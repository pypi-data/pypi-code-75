
from ctypes import *
from ctypes.wintypes import *
from enum import Enum
import time
import platform
import sys
import os
import pkg_resources  # part of setuptools
import enum
import struct
from abc import ABCMeta, abstractmethod
from Anapass  import TDeviceWinDLL
from Anapass.TDeviceBase  import *

#
# class TDevice
#
class TDeviceWin(TDeviceBase) :

    class ErrorString(enum.Enum) :
        GetResp="ErrorGetResp"
    
    def __init__(this, deviceTypeValue):

        TDeviceBase.__init__(this, deviceTypeValue)
        this.__Api = TDeviceWinDLL.Api()
        this.__Api.TSys_WinInit();

        #print(DisplayName +"TRY: create " + deviceType.name )
        this.__DeviceHandle = this.__Api.TDeviceCreate(deviceTypeValue)
        
        #struct TED_POWER_INFO {
        #    TED_S32 no;
        #    TED_S32 available[10];
        #    TED_S32 value1[10];
        #    TED_FLOAT fV[10];
        #    TED_FLOAT fA[10];
        #    TED_FLOAT fRange1[10];
        #    TED_FLOAT fRange2[10];dir

        #};

        this.__PowerStructFmt = 'i'    #    TED_S32 no;    
        this.__PowerStructFmt+='10i'   # TED_S32 available[10];
        this.__PowerStructFmt+='10i'   # TED_S32 value[10];
        this.__PowerStructFmt+='10f'   # TED_FLOAT fV[10];
        this.__PowerStructFmt+='10f'   # TED_FLOAT fV[10];
        this.__PowerStructFmt+='10f'   # TED_FLOAT fRange1[10];
        this.__PowerStructFmt+='10f'   # TED_FLOAT fRange2[10];
        
        # arg=list(range(61))

        this.__PowerStructData = struct.pack(this.__PowerStructFmt, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                           0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                           0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                           0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                           )

    def __del__(this):
        #print("TDevice::~TDevice")
        this.__Api.TDeviceDestroy(this.__DeviceHandle)

            
    def SysSetServerIPAddr(this, serverIPAddr) :
        ret = this.__Api.TDeviceSysSetServerIPAddr(this.__DeviceHandle, TString.ConvertToCTypeStrng(serverIPAddr))
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def SysSetBoardID(this, boardID) : 
        ret = this.__Api.TDeviceSysSetBoardID(this.__DeviceHandle, boardID)
        if ret==1 :
            bflag = True
        else :
            bflag = False
        return bflag

    def SetTcLocalSave(this, boardID, bFlag) : 
        return True #ted.SysSetTcLocalSave(boardID, bFlag)
        
    def Connect(this) :
        ret = this.__Api.TDeviceConnect(this.__DeviceHandle)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def Disonnect(this) :
        ret = this.__Api.TDeviceDisconnect(this.__DeviceHandle)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag
    
    def SendTxtCmd(this, cmd) :
        #print("[this.__Api.TDevice.SendTxtCmd] " + cmd)
        ret = this.__Api.TDeviceSendTxtCmd(this.__DeviceHandle, TString.ConvertToCTypeStrng(cmd), c_char_p(0), 0, 10)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def SendTxtCmdReadResp(this, cmd, maxRespByteSize) :
        respBytesArray=bytes(maxRespByteSize)
        ret = this.__Api.TDeviceSendTxtCmd(this.__DeviceHandle, TString.ConvertToCTypeStrng(cmd), respBytesArray, maxRespByteSize, 1000)
        if ret==1 :
            bflag = True
            resp = TString.ConvertCTypeStringToUnicode(respBytesArray)
        else :
            bflag = False;
            resp = this.__Api.TDevice.ErrorString.GetResp
        return resp

    #private methond
    def SendCtrlCmd(this, cmd) :  
        ret = this.__Api.TDeviceSendCtrlCmd(this.__DeviceHandle, TString.ConvertToCTypeStrng(cmd), c_char_p(0), 0, 0)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def Reset(this) :
        return this.__SendCtrlCmd('RESET')

    def Next(this) :
        return this.__SendCtrlCmd('NEXT')

    def Back(this) :
        return this.__SendCtrlCmd('BACK')

    def ReadReg(this, regAddr, byteOffset, readCount, regValueList, regValueListStartIdx=0) :
        regValueInt = 0
        regValueByteArray=bytes(readCount)
        ret = this.__Api.TDeviceDD_DSIM_MipiReadReg(this.__DeviceHandle, regAddr, byteOffset, readCount, regValueByteArray)
        if ret==1 :
            for idx, regValueByte in enumerate(regValueByteArray) :
                regValueInt = regValueByte
                regValueInt &= 0xFF
                regValueList[idx + regValueListStartIdx] = regValueInt
            bflag = True
        else :
            bflag = False;
        return bflag

    def ReadReg1Byte(this, regAddr, byteOffset) :
        regValueArray=bytes(1)
        ret = this.__Api.TDeviceDD_DSIM_MipiReadReg1Byte(this.__DeviceHandle, regAddr, byteOffset, regValueArray)
        if ret==1 :
            regValue = regValueArray[0]
            regValue &= 0xFF
        else :
            regValue = -1
        return regValue

    def WriteReg(this, regAddr, byteOffset, writeCount, regValueList, writeDataStartIdx=0) :

        if writeDataStartIdx == 0 :
            regValueByteArray=bytes(regValueList)
        else :
            listTmp = regValueList[writeDataStartIdx:(writeDataStartIdx+writeCount)]
            regValueByteArray=bytes(listTmp)

        ret = this.__Api.TDeviceDD_DSIM_MipiWriteReg(this.__DeviceHandle, regAddr, byteOffset, writeCount, regValueByteArray)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def WriteReg1Byte(this, regAddr, byteOffset, regValue) :
        ret = this.__Api.TDeviceDD_DSIM_MipiWriteReg1Byte(this.__DeviceHandle, regAddr, byteOffset, c_char(regValue))
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def WriteCtrlReg(this, regAddr) :
        return this.WriteReg1Byte(regAddr, 0, 1)


    
    def CatchPower(this, powerInfo) :

        ret = this.__Api.TDeviceCatchPowerInfo(this.__DeviceHandle,  this.__PowerStructData, 1000)

        result= struct.unpack(this.__PowerStructFmt, this.__PowerStructData)

        resIdx=0
        
        powerInfo.No = result[resIdx] 
        resIdx += 1

        for i in range(10) :
            powerInfo.Avail[i] = result[i+resIdx]
        resIdx += 10

        for i in range(10) :
            powerInfo.Value1[i] = result[i+resIdx]
        resIdx += 10

        for i in range(10) :
            powerInfo.Voltage[i] = result[i+resIdx]
        resIdx += 10

        for i in range(10) :
            powerInfo.Current[i] = result[i+resIdx]
        resIdx += 10

        for i in range(10) :
            powerInfo.Range1[i] = result[i+resIdx]
        resIdx += 10

        for i in range(10) :
            powerInfo.Range2[i] = result[i+resIdx]
        resIdx += 10

        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    
    
    def DebugMessage(this, msg) :
        #print(msg)
        ret = this.__Api.TDeviceDebugMessage(this.__DeviceHandle, TString.ConvertToCTypeStrng(msg))
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def DebugFuncEnter(this, funcName) :
        ret = this.__Api.TDeviceDebugFuncEnter(this.__DeviceHandle, TString.ConvertToCTypeStrng(funcName))
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def DebugFuncLeave(this, funcName) :
        ret = this.__Api.TDeviceDebugFuncLeave(this.__DeviceHandle, TString.ConvertToCTypeStrng(funcName))
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag
            
    #//VLIN1_ADC
    #TDEVICE_API TED_BOOL this.__Api.TDeviceVlin1AdcSetSamples(TDEVICE_HDL hdl, int value);  
    def Vlin1AdcSetSamples(this, dutIdx, value) :
        ret = this.__Api.TDeviceVlin1AdcSetSamples(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #DEVICE_API TED_BOOL TDeviceVlin1AdcSetInterval(TDEVICE_HDL hdl, int value); 
    def Vlin1AdcSetInterval(this, dutIdx, value) :
        ret = this.__Api.TDeviceVlin1AdcSetInterval(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #TDEVICE_API TED_BOOL TDeviceVlin1AdcSetChannelOn(TDEVICE_HDL hdl, int chIdx);
    def Vlin1AdcSetChannelOn(this, dutIdx, value) :
        ret = this.__Api.TDeviceVlin1AdcSetChannelOn(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #TDEVICE_API TED_BOOL TDeviceVlin1AdcSetChannelOff(TDEVICE_HDL hdl, int chIdx); 
    def Vlin1AdcSetChannelOff(this, dutIdx, value) :
        ret = this.__Api.TDeviceVlin1AdcSetChannelOff(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #TDEVICE_API TED_BOOL TDeviceVlin1AdcSetMode(TDEVICE_HDL hdl, int value);  
    def Vlin1AdcSetMode(this, dutIdx, value) :
        ret = this.__Api.TDeviceVlin1AdcSetMode(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #TDEVICE_API TED_BOOL TDeviceVlin1AdcGetVoltage(TDEVICE_HDL hdl, int chIdx);  
    def Vlin1AdcGetVoltage(this, dutIdx, chIdx) :
        return this.__Api.TDeviceVlin1AdcGetVoltage(this.__DeviceHandle, dutIdx, chIdx)

    #TDEVICE_API TED_BOOL TDeviceVlin1AdcGetVoltageVLIN1(TDEVICE_HDL hdl);  
    def Vlin1AdcGetVoltageVLIN1(this, dutIdx) :
        return this.__Api.TDeviceVlin1AdcGetVoltageVLIN1(this.__DeviceHandle, dutIdx)

    #TDEVICE_API TED_BOOL TDeviceVlin1AdcGetVoltageVBAT(TDEVICE_HDL hdl);  
    def Vlin1AdcGetVoltageVBAT(this, dutIdx) :
        return this.__Api.TDeviceVlin1AdcGetVoltageVBAT(this.__DeviceHandle, dutIdx)

    #TDEVICE_API TED_BOOL TDeviceVlin1AdcGetVoltageELVDD(TDEVICE_HDL hdl);  
    def Vlin1AdcGetVoltageELVDD(this, dutIdx) :
        return this.__Api.TDeviceVlin1AdcGetVoltageELVDD(this.__DeviceHandle, dutIdx)

    #TDEVICE_API TED_BOOL TDeviceVlin1AdcGetCurrent(TDEVICE_HDL hdl, int chIdx);  
    def Vlin1AdcGetCurrent(this, dutIdx, chIdx) :
        return this.__Api.TDeviceVlin1AdcGetCurrent(this.__DeviceHandle, dutIdx, chIdx)

    #TDEVICE_API TED_BOOL TDeviceVlin1AdcGetCurrentVLIN1(TDEVICE_HDL hdl); 
    def Vlin1AdcGetCurrentVLIN1(this, dutIdx) :
        return this.__Api.TDeviceVlin1AdcGetCurrentVLIN1(this.__DeviceHandle, dutIdx)

    #TDEVICE_API TED_BOOL TDeviceVlin1AdcGetCurrentVBAT(TDEVICE_HDL hdl); 
    def Vlin1AdcGetCurrentVBAT(this, dutIdx) :
        return this.__Api.TDeviceVlin1AdcGetCurrentVBAT(this.__DeviceHandle, dutIdx)

    #TDEVICE_API TED_BOOL TDeviceVlin1AdcGetCurrentELVDD(TDEVICE_HDL hdl); 
    def Vlin1AdcGetCurrentELVDD(this, dutIdx) :
        return this.__Api.TDeviceVlin1AdcGetCurrentELVDD(this.__DeviceHandle, dutIdx)

    #//VCI_ADC
    #TDEVICE_API TED_BOOL TDeviceVciAdcSetSamples(TDEVICE_HDL hdl, int value); 
    def VciAdcSetSamples(this, dutIdx, value) :
        ret = this.__Api.TDeviceVciAdcSetSamples(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #TDEVICE_API TED_BOOL TDeviceVciAdcSetInterval(TDEVICE_HDL hdl, int value);
    def VciAdcSetInterval(this, dutIdx, value) :
        ret = this.__Api.TDeviceVciAdcSetInterval(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #TDEVICE_API TED_BOOL TDeviceVciAdcSetChannelOn(TDEVICE_HDL hdl, int chIdx);
    def VciAdcSetChannelOn(this, dutIdx, value) :
        ret = this.__Api.TDeviceVciAdcSetChannelOn(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #TDEVICE_API TED_BOOL TDeviceVciAdcSetChannelOff(TDEVICE_HDL hdl, int chIdx);
    def VciAdcSetChannelOff(this, dutIdx, value) :
        ret = this.__Api.TDeviceVciAdcSetChannelOff(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #TDEVICE_API TED_BOOL TDeviceVciAdcSetMode(TDEVICE_HDL hdl, int value);
    def VciAdcSetMode(this, dutIdx, value) :
        ret = this.__Api.TDeviceVciAdcSetMode(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #TDEVICE_API int TDeviceVciAdcGetVoltage(TDEVICE_HDL hdl, int chIdx);
    def VciAdcGetVoltage(this, dutIdx, chIdx) :
        return this.__Api.TDeviceVciAdcGetVoltage(this.__DeviceHandle, dutIdx, chIdx)

    #TDEVICE_API int TDeviceVciAdcGetVoltageVCI(TDEVICE_HDL hdl);
    def VciAdcGetVoltageVCI(this, dutIdx) :
        return this.__Api.TDeviceVciAdcGetVoltageVCI(this.__DeviceHandle, dutIdx)

    #TDEVICE_API int TDeviceVciAdcGetVoltageVDDR(TDEVICE_HDL hdl);
    def VciAdcGetVoltageVDDR(this, dutIdx) :
        return this.__Api.TDeviceVciAdcGetVoltageVDDR(this.__DeviceHandle, dutIdx)

    #TDEVICE_API int TDeviceVciAdcGetVoltageVDDI(TDEVICE_HDL hdl);
    def VciAdcGetVoltageVDDI(this, dutIdx) :
        return this.__Api.TDeviceVciAdcGetVoltageVDDI(this.__DeviceHandle, dutIdx)

    #TDEVICE_API int TDeviceVciAdcGetCurrent(TDEVICE_HDL hdl, int chIdx);
    def VciAdcGetCurrent(this, dutIdx, chIdx) :
        return this.__Api.TDeviceVciAdcGetCurrent(this.__DeviceHandle, dutIdx, chIdx)

    #DEVICE_API int TDeviceVciAdcGetCurrentVCI(TDEVICE_HDL hdl);
    def VciAdcGetCurrentVCI(this, dutIdx) :
        return this.__Api.TDeviceVciAdcGetCurrentVCI(this.__DeviceHandle, dutIdx)

    #TDEVICE_API int TDeviceVciAdcGetCurrentVDDR(TDEVICE_HDL hdl);
    def VciAdcGetCurrentVDDR(this, dutIdx) :
        return this.__Api.TDeviceVciAdcGetCurrentVDDR(this.__DeviceHandle, dutIdx)

    #TDEVICE_API int TDeviceVciAdcGetCurrentVDDI(TDEVICE_HDL hdl);
    def VciAdcGetCurrentVDDI(this, dutIdx) :
        return this.__Api.TDeviceVciAdcGetCurrentVDDI(this.__DeviceHandle, dutIdx)

    #//SDOUT ADC
    #define TED_SDOUTADC_MAX_CH_COUNT 16
    #TDEVICE_API int TDeviceSoutAdcSetDevConfig(TDEVICE_HDL hdl, int value);
    def SoutAdcSetDevConfig(this, dutIdx, value) :
        ret = this.__Api.TDeviceSoutAdcSetDevConfig(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #TDEVICE_API int TDeviceSoutAdcSetInConfig(TDEVICE_HDL hdl, int chIdx,  int value); 
    def SoutAdcSetInConfig(this, chIdx, dutIdx, value) :
        ret = this.__Api.TDeviceSoutAdcSetInConfig(this.__DeviceHandle, dutIdx, chIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #DEVICE_API int TDeviceSoutAdcSetRBSel(TDEVICE_HDL hdl, int value);    
    def SoutAdcSetRBSel(this, dutIdx, value) :
        ret = this.__Api.TDeviceSoutAdcSetRBSel(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #TDEVICE_API int TDeviceSoutAdcGetChannelCount(TDEVICE_HDL hdl);
    def SoutAdcGetChannelCount(this, dutIdx) :
        return this.__Api.TDeviceSoutAdcGetChannelCount(this.__DeviceHandle, dutIdx)

    #TDEVICE_API int TDeviceSoutAdcGetVoltage(TDEVICE_HDL hdl, int chIdx);  
    def SoutAdcGetVoltage(this, dutIdx, chIdx) :
        return this.__Api.TDeviceSoutAdcGetVoltage(this.__DeviceHandle, dutIdx, chIdx)

    #TDEVICE_API TED_BOOL TDeviceSoutAdcGetAllVoltage(TDEVICE_HDL hdl, int* voltageArray);
    def SoutAdcGetAllVoltage(this, dutIdx) :

        structFmt = 'i'    #    TED_S32 no;    
        for i in range(15) :
            structFmt += 'i'    #    TED_S32 no;    
        structData = struct.pack(structFmt, 
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           )
        voltageList=[-1 for _ in range(16)]
        ret = this.__Api.TDeviceSoutAdcGetAllVoltage(this.__DeviceHandle, dutIdx, structData)
        if ret==1 :
            result= struct.unpack(structFmt, structData)
            for i in range(16) :
                voltageList[i] = result[i]
        return voltageList


    #TDEVICE_API TED_BOOL TDeviceLdoAdcSetInConfig(TDEVICE_HDL hdl, int chIdx, int value);
    def LdoAdcSetInConfig(this, dutIdx, chIdx, value) :
        ret = this.__Api.TDeviceLdoAdcSetInConfig(this.__DeviceHandle, dutIdx, chIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #TDEVICE_API int TDeviceLdoAdcGetChannelCount(TDEVICE_HDL hdl);
    def LdoAdcGetChannelCount(this, dutIdx) :
        return this.__Api.TDeviceLdoAdcGetChannelCount(this.__DeviceHandle, dutIdx)

    #TDEVICE_API int TDeviceLdoAdcGetVoltage(TDEVICE_HDL hdl, int chIdx);
    def LdoAdcGetVoltage(this, dutIdx, chIdx) :
        return this.__Api.TDeviceLdoAdcGetVoltage(this.__DeviceHandle, dutIdx, chIdx)

    #TDEVICE_API TED_BOOL TDeviceLdoAdcGetAllVoltage(TDEVICE_HDL hdl, int* voltageArray);
    def LdoAdcGetAllVoltage(this, dutIdx) :

        structFmt = 'i'    #    TED_S32 no;    
        for i in range(15) :
            structFmt += 'i'    #    TED_S32 no;    
        structData = struct.pack(structFmt, 
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           )
        voltageList=[-1 for _ in range(16)]
        ret = this.__Api.TDeviceLdoAdcGetAllVoltage(this.__DeviceHandle, dutIdx, structData)
        if ret==1 :
            result= struct.unpack(structFmt, structData)
            for i in range(16) :
                voltageList[i] = result[i]
        return voltageList


    #TDEVICE_API TED_BOOL TDeviceRegAdcSetInConfig(TDEVICE_HDL hdl, int chIdx, int value);
    def RegAdcSetInConfig(this, dutIdx, chIdx, value) :
        ret = this.__Api.TDeviceRegAdcSetInConfig(this.__DeviceHandle, dutIdx, chIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #TDEVICE_API int TDeviceRegAdcGetChannelCount(TDEVICE_HDL hdl);
    def RegAdcGetChannelCount(this, dutIdx) :
        return this.__Api.TDeviceRegAdcGetChannelCount(this.__DeviceHandle, dutIdx)

    #TDEVICE_API int TDeviceRegAdcGetVoltage(TDEVICE_HDL hdl, int chIdx);
    def RegAdcGetVoltage(this, dutIdx, chIdx) :
        return this.__Api.TDeviceRegAdcGetVoltage(this.__DeviceHandle, dutIdx, chIdx)

    #TDEVICE_API TED_BOOL TDeviceLdoAdcGetAllVoltage(TDEVICE_HDL hdl, int* voltageArray);
    def RegAdcGetAllVoltage(this, dutIdx) :

        structFmt = 'i'    #    TED_S32 no;    
        for i in range(15) :
            structFmt += 'i'    #    TED_S32 no;    
        structData = struct.pack(structFmt, 
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           )
        voltageList=[-1 for _ in range(16)]
        ret = this.__Api.TDeviceRegAdcGetAllVoltage(this.__DeviceHandle, dutIdx, structData)
        if ret==1 :
            result= struct.unpack(structFmt, structData)
            for i in range(16) :
                voltageList[i] = result[i]
        return voltageList

    def AgingNotifyPyStart(this, pyFileName) : 
        ret = this.__Api.TDeviceAgingNotifyPyStart(this.__DeviceHandle, TString.ConvertToCTypeStrng(pyFileName))
        if ret==1 :
            bflag = True
        else :
            bflag = False
        return bflag

    def AgingNotifyPyStop(this, pyFileName) : 
        ret = this.__Api.TDeviceAgingNotifyPyStop(this.__DeviceHandle, TString.ConvertToCTypeStrng(pyFileName))
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #TDEVICE_API TED_BOOL TDeviceAgingSetCurJobInfo(TDEVICE_HDL hdl, int jobID, int status, int scIdx, int scCount, const char* desc);
    def AgingSetCurJobInfo(this, dutIdx, jobID, status, scIdx, scCount, desc) :
        return this.__Api.TDeviceAgingSetCurJobInfo(this.__DeviceHandle, dutIdx, jobID, status,scIdx, scCount, TString.ConvertToCTypeStrng(desc))

    #TDEVICE_API TED_BOOL TDeviceAgingSetCurScInfo(TDEVICE_HDL hdl, int scID, int status, int tcIdx, int tcCount, const char* desc);
    def AgingSetCurScInfo(this, dutIdx, scID, status,tcIdx, tcCount, desc) :
        return this.__Api.TDeviceAgingSetCurScInfo(this.__DeviceHandle, dutIdx, scID, status,tcIdx, tcCount, TString.ConvertToCTypeStrng(desc))

    #TDEVICE_API TED_BOOL TDeviceAgingSetCurTcInfo(void* hdl, int dutIdx, int tcID, int status, int tcStepIdx, int tcStepCount, const char* desc);
    def AgingSetCurTcInfo(this, dutIdx, tcID, status, tcStepIdx, tcStepCount, desc) :
        return this.__Api.TDeviceAgingSetCurTcInfo(this.__DeviceHandle, dutIdx, tcID, status, tcStepIdx, tcStepCount, TString.ConvertToCTypeStrng(desc))

    #TDEVICE_API TED_BOOL TDeviceAgingSetCurTcStepInfo(TDEVICE_HDL hdl, int tcStepID, int status, const char* desc);
    def AgingSetCurTcStepInfo(this, dutIdx, tcStepID, status, desc) :
        return this.__Api.TDeviceAgingSetCurTcStepInfo(this.__DeviceHandle, dutIdx, tcStepID, status, TString.ConvertToCTypeStrng(desc))

    #TDEVICE_API  TED_BOOL TDeviceAgingMeasureADC(TDEVICE_HDL hdl, int jobID, int scID, int tcID, int tcStep,  const char* desc, /*OUT*/unsigned char* res);
    def AgingMeasureADC(this, dutIdx) : 
        #soutChannelCount = this.SoutAdcGetChannelCount()
        #ldoChannelCount = this.LdoAdcGetChannelCount()
        #regChannelCount = this.RegAdcGetChannelCount()
        #meaRes = Adc.Measure(soutChannelCount, ldoChannelCount, regChannelCount)
        ##this.__Api.TDeviceAgingMeasureADC(this.__DeviceHandle, dutIdx, meaRes.GetStructData())
        #meaRes.ParseStructData()
        #return meaRes
        this.__Api.TDeviceAgingMeasureADC(this.__DeviceHandle, dutIdx, None)
        #return True

    #COMM_API int TedAgingMeasureADCResultStructureByteSize();
    def AgingMeasureADCResultStructureByteSize(this) : 
        return this.__Api.TDeviceAgingMeasureADCResultStructureByteSize()
            
    def ANA670X_GetChipIDCount(this) : 
        return 1  #ted.ANA670X_GetChipIDCount()

    def ANA670X_GetChipID(this, dutIdx) : 
        return 1 #ted.ANA670X_GetChipID(dutIdx)

    def ANA670X_GetProductRevisionBytesCount(this) : 
        return 1 #ted.ANA670X_GetProductRevisionBytesCount()

    def ANA670X_GetProductRevisionBytes(this, dutIdx) : 
        return 1 #ted.ANA670X_GetProductRevisionBytes(dutIdx)

    def ANA670X_SetFrameRate(this, dutIdx, fr) :
        return True #ted.ANA670X_SetFrameRate(dutIdx, fr)

    def ANA670X_GetFrameRate(this, dutIdx) : 
        return 1 #ted.ANA670X_GetFrameRate(dutIdx)

    #COMM_API Bool TedAdcSoutSetRBSel(int dutIdx, int value)
    def AdcSoutSetRBSel(this, dutIdx, value) :
        return True #ted.AdcSoutSetRBSel(dutIdx, value)

    #COMM_API int TedAdcSoutGetRBSel(int dutIdx)
    def AdcSoutGetRBSel(this, dutIdx) :
        return 1 #ted.AdcSoutGetRBSel(dutIdx)


    #COMM_API Bool TedDD_DSIM_MipiReadReg(int dutIdx, int addr, int byteOffset, int readCount, unsigned char* buf, int bufMaxByteSize);
    def DD_DSIM_MipiReadReg(this, dutIdx, regAddr, byteOffset, readCount) : 
        return 1 #ted.DD_DSIM_MipiReadReg(dutIdx, regAddr, byteOffset, readCount)

    #COMM_API unsigned char TedDD_DSIM_MipiReadReg1Byte(int dutIdx, int addr, int byteOffset);
    def DD_DSIM_MipiReadReg1Byte(this, dutIdx, regAddr, byteOffset) : 
        return 1 #ted.DD_DSIM_MipiReadReg1Byte(dutIdx, regAddr, byteOffset)

    #COMM_API Bool TedDD_DSIM_MipiReadReg(int dutIdx, int addr, int byteOffset, int readCount, unsigned char* buf, int bufMaxByteSize);
    def DD_DSIM_MipiWriteReg(this, dutIdx, regAddr, byteOffset, regValueList) : 
        return 1 #ted.DD_DSIM_MipiWriteReg(dutIdx, regAddr, byteOffset, regValueList)

    #COMM_API Bool TedDD_DSIM_MipiWriteReg1Byte(int dutIdx, int addr, int byteOffset, unsigned char data);
    def DD_DSIM_MipiWriteReg1Byte(this, dutIdx, regAddr, byteOffset, regValue) : 
        return 1 #ted.DD_DSIM_MipiWriteReg1Byte(dutIdx, regAddr, byteOffset, regValue)

    #WREG0=0x39, [Addr], [regVal0], [regVal1].....
    def DD_DSIM_MipiWriteReg39(this, dutIdx, regAddr, regValueList) :
        #print("[this.__Api.TDevice.DD_DSIM_MipiWriteReg39] 0x%02x" % (regAddr))
        regValueByteArray=bytes(regValueList)
        ret = this.__Api.TDeviceDD_DSIM_MipiWriteReg39(this.__DeviceHandle, regAddr, len(regValueList), regValueByteArray)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #WREG0=0x15, [Addr], [regVal]
    def DD_DSIM_MipiWriteReg15(this, dutIdx, regAddr, regValue) :

        #print("[this.__Api.TDevice.DD_DSIM_MipiWriteReg15] 0x%02x" % (regAddr))

        ret = this.__Api.TDeviceDD_DSIM_MipiWriteReg15(this.__DeviceHandle, regAddr, regValue)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #WREG0=0x05, [Addr]
    def DD_DSIM_MipiWriteReg05(this, dutIdx, regAddr) :

        #print("[this.__Api.TDevice.DD_DSIM_MipiWriteReg05] 0x%02x" % (regAddr))

        ret = this.__Api.TDeviceDD_DSIM_MipiWriteReg05(this.__DeviceHandle, regAddr)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #WREG0=0x07, [value]   :   Compressd Mode Command
    def DD_DSIM_MipiWriteReg07(this, dutIdx, value) :
        ret = this.__Api.TDeviceDD_DSIM_MipiWriteReg07(this.__DeviceHandle, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    
    
    def DD_DSIM_manual_ctrl(this, dutIdx, value) :
        ret = this.__Api.TDeviceDD_DSIM_manual_ctrl(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag
        

    #COMM_API Bool TedDD_DSIM_power_ctrl(int dutIdx, int value);
    def DD_DSIM_power_ctrl(this, dutIdx, value) :
        ret = this.__Api.TDeviceDD_DSIM_power_ctrl(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #COMM_API Bool TedDD_DSIM_source_cal(int dutIdx, int value);
    def DD_DSIM_source_cal(this, dutIdx, value) :
        ret = this.__Api.TDeviceDD_DSIM_source_cal(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def DD_DSIM_sleepin(this, dutIdx, value) : 
        ret = this.__Api.TDeviceDD_DSIM_sleepin(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag
    
    def DD_DSIM_sleepout(this, dutIdx, value) : 
        ret = this.__Api.TDeviceDD_DSIM_sleepout(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag
    
    def DD_DSIM_deep_standby(this, dutIdx, value) : 
        ret = this.__Api.TDeviceDD_DSIM_deep_standby(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag
    
    def DD_DSIM_displayon(this, dutIdx, value) : 
        ret = this.__Api.TDeviceDD_DSIM_displayon(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag
    
    def DD_DSIM_reset_ctrl(this, dutIdx, value) : 
        ret = this.__Api.TDeviceDD_DSIM_reset_ctrl(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag
    
    def DD_FB_blank(this, dutIdx, value) :
        ret = this.__Api.TDeviceDD_FB_blank(this.__DeviceHandle, dutIdx, value)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def PatternConnect(this) : 
        ret = this.__Api.TDevicePatternConnect(this.__DeviceHandle)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def PatternDisconnect(this) : 
        ret = this.__Api.TDevicePatternDisconnect(this.__DeviceHandle)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def PatternIsConnect(this) : 
        ret = this.__Api.TDevicePatternIsConnect(this.__DeviceHandle)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag


    def PatternSetCommand(this, ptrnCmd) :
        ret = this.__Api.TDevicePatternSetCommand(this.__DeviceHandle, TString.ConvertToCTypeStrng(ptrnCmd))
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag
    
    def PatternPaint(this, r, g, b, a) : 
        ret = this.__Api.TDevicePatternPaint(this.__DeviceHandle, r, g, b, a)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def PatternUpdateScreen(this) : 
        ret = this.__Api.TDevicePatternUpdateScreen(this.__DeviceHandle)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def PatternDrawImage(this, imgFileName) : 
        ret = this.__Api.TDevicePatternDrawImage(this.__DeviceHandle, imgFileName)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def PatternScreenVerify(this, r, g, b) : 
        ret = this.__Api.TDevicePatternScreenVerify(this.__DeviceHandle, r, g, b)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    
    def SysGetCurUtcTime(this) : 
        return this.__Api.TDeviceSysGetCurUtcTime(this.__DeviceHandle)

    def SysDelay(this, delay) :
        ret = this.__Api.TDeviceSysDelay(this.__DeviceHandle, delay)
        if ret==1 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def SysGetDutIndexAllDeviceValue(this) : 
        return this.__Api.TDeviceSysGetDutIndexAllDeviceValue(this.__DeviceHandle)

    def SysGetDutCount(this) : 
        return this.__Api.TDeviceSysGetDutCount(this.__DeviceHandle)

    def SysGetTickCount64(this) : 
        return this.__Api.TDeviceSysGetTickCount64(this.__DeviceHandle)
    
    def SysGetUtcTimeKST(this, year, month, day, hour, min, sec) : 
        return this.__Api.TDeviceSysGetUtcTimeKST(this.__DeviceHandle, year, month, day, hour, min, sec)

    def SysGetErrFlag(this) : 
        return this.__Api.TDeviceSysGetErrFlag(this.__DeviceHandle)

    def SysMipiLock(this) : 
        return this.__Api.TDeviceSysMipiLock(this.__DeviceHandle)

    def SysMipiUnlock(this) : 
        return this.__Api.TDeviceSysMipiUnlock(this.__DeviceHandle)

    def SysMipiIsLock(this) : 
        return this.__Api.TDeviceSysMipiIsLock(this.__DeviceHandle)


#
# class TFileTransfer
#
class TFileTransfer :

    class Type(enum.IntEnum) : 
        T5 = 0
        
    class ErrorType(enum.IntEnum) : 
        Success = 0,
        SendPacket=1,
        NoResp=2,
        FileOpen=3,
        StorageSize=4,
        CRC=5
    
    #TDEVICE_API TFILETRANSFER_HDL TFileTransferCreate(enum TFileTransferType type, TDEVICE_HDL deviceHandle);
    def __init__(this, type, device) :
        this.__TFileTransferHandle = TFileTransferCreate(type, device.Handle)
        this.__FileName = ""

    def __getattr__(this, attrName) :
        if attrName == 'LastErrorString' : 
            return this.GetLastErrorString()
        if attrName == 'FileName' : 
            return this.__FileName
        else :
            raise AttributeError(attrName)


    #TDEVICE_API TED_BOOL TFileTransferDestroy(TFILETRANSFER_HDL fileTransferHandle);

    #TDEVICE_API TED_BOOL TFileTransferStart(TFILETRANSFER_HDL fileTransferHandle, const char* fileName);
    def Start(this, fileName) : 
        this.__FileName = fileName
        bytesString = fileName.encode('euc-kr')
        #bytesString = fileName.encode('ascii')
        #bytesString = fileName.encode('utf-8')
        ret = TFileTransferStart(this.__TFileTransferHandle, bytesString)
        return ret

    #TDEVICE_API TED_BOOL TFileTransferStop(TFILETRANSFER_HDL fileTransferHandle);
    def Stop(this) : 
        ret = TFileTransferStop(this.__TFileTransferHandle)
        return ret

    #TDEVICE_API int TFileTransferGetFileByteSize(TFILETRANSFER_HDL fileTransferHandle);
    def GetFileByteSize(this) : 
        ret = TFileTransferGetFileByteSize(this.__TFileTransferHandle)
        return ret

    #TDEVICE_API int TFileTransferGetTransferByteSize(TFILETRANSFER_HDL fileTransferHandle);
    def GetTransferByteSize(this) : 
        ret = TFileTransferGetTransferByteSize(this.__TFileTransferHandle)
        return ret

    #TDEVICE_API TED_BOOL TFileTransferIsStart(TFILETRANSFER_HDL fileTransferHandle);
    def IsStart(this) : 
        ret = TFileTransferIsStart(this.__TFileTransferHandle)
        return ret

    #TDEVICE_API TED_BOOL TFileTransferIsDone(TFILETRANSFER_HDL fileTransferHandle);
    def IsDone(this) : 
        ret = TFileTransferIsDone(this.__TFileTransferHandle)
        return ret

    #TDEVICE_API TED_BOOL TFileTransferIsError(TFILETRANSFER_HDL fileTransferHandle);
    def IsError(this) : 
        ret = TFileTransferIsError(this.__TFileTransferHandle)
        return ret

    #TDEVICE_API enum TFileTransferError TFileTransferGetLastError(TFILETRANSFER_HDL fileTransferHandle);
    def GetLastError(this) : 
        ret = TFileTransferGetLastError(this.__TFileTransferHandle)
        return ret

    def GetLastErrorString(this) :
        err = this.GetLastError()
        if err == TFileTransfer.ErrorType.Success :
            return "Success"
        elif err == TFileTransfer.ErrorType.SendPacket :
            return "SendPacket Error"
        elif err == TFileTransfer.ErrorType.NoResp :
            return "NoResp Error"
        elif err == TFileTransfer.ErrorType.FileOpen :
            return "FileOpen Error"
        elif err == TFileTransfer.ErrorType.StorageSize :
            return "StorageSize Error"
        elif err == TFileTransfer.ErrorType.CRC :
            return "CRC Error"
        else :
            return "Unknown Error"
    
    