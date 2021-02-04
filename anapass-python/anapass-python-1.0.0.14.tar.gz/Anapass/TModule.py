import platform
import enum
from Anapass.TDeviceBase import *

if platform.system()=="Windows" : 
    from Anapass.TDeviceWin import *
else :
    from Anapass.TDeviceAndroid import *

class TDevice :

    class Type(enum.IntEnum) : 
        T5 = 0
        T5PacketAnalysis=1
        T4 = 2
        TESys=3
    
    def __init__(this, deviceType): 

        if platform.system()=="Windows" : 
            print("os is windows")
            this.__TDevice = TDeviceWin(deviceType.value)
        else :
            this.__TDevice = TDeviceAndroid(deviceType.value)

        this.__DeviceType = deviceType

        #Staticts
        this.__AgingMeasureAdcCount = 0


    def __getattr__(this, attrName) :
        
        if attrName == 'Message' :
            return this.DebugMessage
        
        elif attrName == 'PTRN_SET' :
            return this.PatternSetCommand
        
        elif attrName == 'WREG0_39' :
            return this.DD_DSIM_MipiWriteReg39
        
        elif attrName == 'WREG0_15' :
            return this.DD_DSIM_MipiWriteReg15
        
        elif attrName == 'WREG0_05' :
            return this.DD_DSIM_MipiWriteReg05

        elif attrName == 'WREG0_07' :
            return this.DD_DSIM_MipiWriteReg07
        
        elif attrName == 'RREG1Byte' :
            return this.DD_DSIM_MipiReadReg1Byte
        
        elif attrName == 'RREG' :
            return this.DD_DSIM_MipiReadReg
        
        elif attrName == 'WREG1Byte' :
            return this.DD_DSIM_MipiWriteReg1Byte
        
        elif attrName == 'WREG' :
            return this.DD_DSIM_MipiWriteReg
        
        elif attrName == 'DelayMS' :
            return this.SysDelay

        else :
            raise AttributeError(attrName)


    def GetName(this) :
        return this.__DeviceType.name

    def SysSetServerIPAddr(this, serverIPAddr) : 
        return this.__TDevice.SysSetServerIPAddr(serverIPAddr);
    
    def Connect(this) : 
        return this.__TDevice.Connect()

    def Disonnect(this) : 
        return this.__TDevice.Disonnect()

    def SysSetBoardID(this, boardID) : 
        return this.__TDevice.SysSetBoardID(boardID)
    
    def SetTcLocalSave(this, boardID, bFlag) : 
        return this.__TDevice.SetTcLocalSave(boardID, bFlag)
        
    def SysGetDutIndexAllDeviceValue(this) : 
        return this.__TDevice.SysGetDutIndexAllDeviceValue()

    def SysGetDutCount(this) : 
        return this.__TDevice.SysGetDutCount()

    def SysGetTickCount64(this) : 
        return this.__TDevice.SysGetTickCount64()

    def SysGetCurUtcTime(this) : 
        return this.__TDevice.SysGetCurUtcTime()

    def SysGetUtcTimeKST(this, year, month, day, hour, min, sec) : 
        return this.__TDevice.SysGetUtcTimeKST(year, month, day, hour, min, sec)

    def SysGetErrFlag(this) : 
        return this.__TDevice.SysGetErrFlag()

    def SysMipiLock(this) : 
        return this.__TDevice.SysMipiLock()

    def SysMipiUnlock(this) : 
        return this.__TDevice.SysMipiUnlock()

    def SysMipiIsLock(this) : 
        return this.__TDevice.SysMipiIsLock()

    def SendTxtCmd(this, cmd) : 
        return this.__TDevice.SendTxtCmd(cmd)

    def SendTxtCmdReadResp(this, cmd, maxRespByteSize) : 
        return this.__TDevice.SendTxtCmdReadResp(cmd, maxRespByteSize)

    def SendCtrlCmd(this, cmd) :  
        return this.__TDevice.SendCtrlCmd(cmd)

    def Reset(this) :
        return this.__TDevice.Reset()

    def Next(this) :
        return this.__TDevice.Next()

    def Back(this) :
        return this.__TDevice.Back()

    def ReadReg(this, regAddr, byteOffset, readCount, regValueList, regValueListStartIdx=0) : 
        
        dutIndex = 0
        regValueInt = 0
        regValueByteArray=bytes(readCount)
        ret = this.__TDevice.DD_DSIM_MipiReadReg(this.__DeviceHandle, regAddr, byteOffset, readCount, regValueByteArray)
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
        return this.__TDevice.ReadReg1Byte(regAddr, byteOffset)

    def WriteReg(this, regAddr, byteOffset, writeCount, regValueList, writeDataStartIdx=0) : 
        return this.__TDevice.WriteReg(regAddr, byteOffset, writeCount, regValueList, writeDataStartIdx)

    def WriteReg1Byte(this, regAddr, byteOffset, regValue) : 
        return this.__TDevice.WriteReg1Byte(regAddr, byteOffset, regValue)
        
    def WriteCtrlReg(this, regAddr) : 
        return this.__TDevice.WriteCtrlReg(regAddr)

    #COMM_API Bool TedDD_DSIM_MipiReadReg(int dutIdx, int addr, int byteOffset, int readCount, unsigned char* buf, int bufMaxByteSize);
    def DD_DSIM_MipiReadReg(this, dutIdx, regAddr, byteOffset, readCount) : 
        return this.__TDevice.DD_DSIM_MipiReadReg(dutIdx, regAddr, byteOffset, readCount)

    def DD_DSIM_MipiReadReg1Byte(this, dutIdx, regAddr, byteOffset) : 
        return this.__TDevice.DD_DSIM_MipiReadReg1Byte(dutIdx, regAddr, byteOffset)

    #COMM_API Bool TedDD_DSIM_MipiReadReg(int dutIdx, int addr, int byteOffset, int readCount, unsigned char* buf, int bufMaxByteSize);
    def DD_DSIM_MipiWriteReg(this, dutIdx, regAddr, byteOffset, regValueList) : 
        return this.__TDevice.DD_DSIM_MipiWriteReg(dutIdx, regAddr, byteOffset, regValueList)

    #COMM_API Bool TedDD_DSIM_MipiWriteReg1Byte(int dutIdx, int addr, int byteOffset, unsigned char data);
    def DD_DSIM_MipiWriteReg1Byte(this, dutIdx, regAddr, byteOffset, regValue) : 
        return this.__TDevice.DD_DSIM_MipiWriteReg1Byte(dutIdx, regAddr, byteOffset, regValue)

    #WREG0=0x39, [Addr], [regVal0], [regVal1].....
    def DD_DSIM_MipiWriteReg39(this, dutIdx, regAddr, regValueList) : 
        return this.__TDevice.DD_DSIM_MipiWriteReg39(dutIdx, regAddr, regValueList)

    #WREG0=0x15, [Addr], [regVal]
    def DD_DSIM_MipiWriteReg15(this, dutIdx, regAddr, regValue) : 
        return this.__TDevice.DD_DSIM_MipiWriteReg15(dutIdx, regAddr, regValue)

    #WREG0=0x05, [Addr]
    def DD_DSIM_MipiWriteReg05(this, dutIdx, regAddr) : 
        return this.__TDevice.DD_DSIM_MipiWriteReg05(dutIdx, regAddr)

    #WREG0=0x07, [value]   :   Compressd Mode Command
    def DD_DSIM_MipiWriteReg07(this, dutIdx, value) : 
        return this.__TDevice.DD_DSIM_MipiWriteReg07(dutIdx, value)
        
    def CatchPower(this, powerInfo) : 
        return this.__TDevice.CatchPower(powerInfo)

    def PatternConnect(this) : 
        return this.__TDevice.PatternConnect()

    def PatternDisconnect(this) : 
        return this.__TDevice.PatternDisconnect()

    def PatternIsConnect(this) : 
        return this.__TDevice.PatternIsConnect()

    def PatternSetCommand(this, ptrnCmd) : 
        return this.__TDevice.PatternSetCommand(ptrnCmd)

    def PatternPaint(this, r, g, b, a) : 
        return this.__TDevice.PatternPaint(r, g, b, a)

    def PatternUpdateScreen(this) : 
        return this.__TDevice.PatternUpdateScreen()

    def PatternScreenVerify(this, r, g, b) : 
        return this.__TDevice.PatternScreenVerify(r, g, b)

    def PatternDrawImage(this, imgFileName) : 
        return this.__TDevice.PatternDrawImage(imgFileName)

    def ANA670X_GetChipIDCount(this) : 
        return this.__TDevice.ANA670X_GetChipIDCount()

    def ANA670X_GetChipID(this, dutIdx) : 
        return this.__TDevice.ANA670X_GetChipID(dutIdx)

    def ANA670X_GetProductRevisionBytesCount(this) : 
        return this.__TDevice.ANA670X_GetProductRevisionBytesCount()

    def ANA670X_GetProductRevisionBytes(this, dutIdx) : 
        return this.__TDevice.ANA670X_GetProductRevisionBytes(dutIdx)

    def ANA670X_SetFrameRate(this, dutIdx, fr) :
        return this.__TDevice.ANA670X_SetFrameRate(dutIdx, fr)

    def ANA670X_GetFrameRate(this, dutIdx) : 
        return this.__TDevice.ANA670X_GetFrameRate(dutIdx)

    def SysDelay(this, delay) : 
        return this.__TDevice.SysDelay(delay)
        
    def DebugMessage(this, msg) : 
        return this.__TDevice.DebugMessage(msg)
        
    def DebugFuncEnter(this, funcName) : 
        return this.__TDevice.DebugFuncEnter(funcName)
    
    def DebugFuncLeave(this, funcName) : 
        return this.__TDevice.DebugFuncLeave(funcName)
    
    def DD_FB_blank(this, dutIdx, value) : 
        return this.__TDevice.DD_FB_blank(dutIdx, value)

    def DD_DSIM_manual_ctrl(this, dutIdx, value) : 
        return this.__TDevice.DD_DSIM_manual_ctrl(dutIdx, value)

    def DD_DSIM_power_ctrl(this, dutIdx, value) : 
        return this.__TDevice.DD_DSIM_power_ctrl(dutIdx, value)

    def DD_DSIM_source_cal(this, dutIdx, value) : 
        return this.__TDevice.DD_DSIM_source_cal(dutIdx, value)

    def DD_DSIM_sleepin(this, dutIdx, value) : 
        return this.__TDevice.DD_DSIM_sleepin(dutIdx, value)
    
    def DD_DSIM_sleepout(this, dutIdx, value) : 
        return this.__TDevice.DD_DSIM_sleepout(dutIdx, value)
    
    def DD_DSIM_deep_standby(this, dutIdx, value) : 
        return this.__TDevice.DD_DSIM_deep_standby(dutIdx, value)
    
    def DD_DSIM_displayon(this, dutIdx, value) : 
        return this.__TDevice.DD_DSIM_displayon(dutIdx, value)
    
    def DD_DSIM_reset_ctrl(this, dutIdx, value) : 
        return this.__TDevice.DD_DSIM_reset_ctrl(dutIdx, value)


    #//VLIN1_ADC
    def Vlin1AdcSetSamples(this, value) : 
        return this.__TDevice.Vlin1AdcSetSamples(value)

    def Vlin1AdcSetInterval(this, value) : 
        return this.__TDevice.Vlin1AdcSetInterval(value)

    def Vlin1AdcSetChannelOn(this, value) : 
        return this.__TDevice.Vlin1AdcSetChannelOn(value)

    def Vlin1AdcSetChannelOff(this, value) : 
        return this.__TDevice.Vlin1AdcSetChannelOff(value)

    def Vlin1AdcSetMode(this, value) : 
        return this.__TDevice.Vlin1AdcSetMode(value)

    def Vlin1AdcGetVoltage(this, chIdx) : 
        return this.__TDevice.Vlin1AdcGetVoltage(chIdx)

    def Vlin1AdcGetVoltageVLIN1(this) : 
        return this.__TDevice.Vlin1AdcGetVoltageVLIN1()

    def Vlin1AdcGetVoltageVBAT(this) : 
        return this.__TDevice.Vlin1AdcGetVoltageVBAT()

    def Vlin1AdcGetVoltageELVDD(this) : 
        return this.__TDevice.Vlin1AdcGetVoltageELVDD()

    def Vlin1AdcGetCurrent(this, chIdx) : 
        return this.__TDevice.Vlin1AdcGetCurrent(chIdx)

    def Vlin1AdcGetCurrentVLIN1(this) : 
        return this.__TDevice.Vlin1AdcGetCurrentVLIN1()

    def Vlin1AdcGetCurrentVBAT(this) : 
        return this.__TDevice.Vlin1AdcGetCurrentVBAT()

    def Vlin1AdcGetCurrentELVDD(this) : 
        return this.__TDevice.Vlin1AdcGetCurrentELVDD()

    #//VCI_ADC
    def VciAdcSetSamples(this, value) : 
        return this.__TDevice.VciAdcSetSamples(value)

    def VciAdcSetInterval(this, value) : 
        return this.__TDevice.VciAdcSetInterval(value)

    def VciAdcSetChannelOn(this, value) : 
        return this.__TDevice.VciAdcSetChannelOn(value)

    def VciAdcSetChannelOff(this, value) : 
        return this.__TDevice.VciAdcSetChannelOff(value)

    def VciAdcSetMode(this, value) : 
        return this.__TDevice.VciAdcSetMode(value)
        
    def VciAdcGetVoltage(this, chIdx) : 
        return this.__TDevice.VciAdcGetVoltage(chIdx)

    def VciAdcGetVoltageVCI(this) : 
        return this.__TDevice.VciAdcGetVoltageVCI()

    def VciAdcGetVoltageVDDR(this) : 
        return this.__TDevice.VciAdcGetVoltageVDDR()

    def VciAdcGetVoltageVDDI(this) : 
        return this.__TDevice.VciAdcGetVoltageVDDI()

    def VciAdcGetCurrent(this, chIdx) : 
        return this.__TDevice.VciAdcGetCurrent(chIdx)

    def VciAdcGetCurrentVCI(this) : 
        return this.__TDevice.VciAdcGetCurrentVCI()

    def VciAdcGetCurrentVDDR(this) : 
        return this.__TDevice.VciAdcGetCurrentVDDR()

    def VciAdcGetCurrentVDDI(this) : 
        return this.__TDevice.VciAdcGetCurrentVDDI()

    #//SDOUT ADC
    def SoutAdcSetDevConfig(this, value) : 
        return this.__TDevice.SoutAdcSetDevConfig(value)

    def SoutAdcSetInConfig(this, chIdx, value) : 
        return this.__TDevice.SoutAdcSetInConfig(chIdx, value)

    def AdcSoutSetRBSel(this, dutIdx, value) : 
        return this.__TDevice.AdcSoutSetRBSel(dutIdx, value)

    def AdcSoutGetRBSel(this, dutIdx) : 
        return this.__TDevice.AdcSoutGetRBSel(dutIdx)

    def SoutAdcGetChannelCount(this) : 
        return this.__TDevice.SoutAdcGetChannelCount()

    def SoutAdcGetVoltage(this, chIdx) : 
        return this.__TDevice.SoutAdcGetVoltage(chIdx)

    def SoutAdcGetAllVoltage(this) : 
        return this.__TDevice.SoutAdcGetVoltage(chIdx)

    def LdoAdcSetInConfig(this, chIdx, value) : 
        return this.__TDevice.LdoAdcSetInConfig(chIdx, value)

    def LdoAdcGetChannelCount(this) : 
        return this.__TDevice.LdoAdcGetChannelCount()

    def LdoAdcGetVoltage(this, chIdx) : 
        return this.__TDevice.LdoAdcGetVoltage(chIdx)

    def LdoAdcGetAllVoltage(this) : 
        return this.__TDevice.LdoAdcGetAllVoltage()

    def RegAdcSetInConfig(this, chIdx, value) : 
        return this.__TDevice.RegAdcSetInConfig(chIdx, value)

    def RegAdcGetChannelCount(this) : 
        return this.__TDevice.RegAdcGetChannelCount()

    def RegAdcGetVoltage(this, chIdx) : 
        return this.__TDevice.RegAdcGetVoltage(chIdx)

    def RegAdcGetAllVoltage(this) : 
        return this.__TDevice.RegAdcGetAllVoltage()

    def AgingNotifyPyStart(this, pyFileName) : 
        return this.__TDevice.AgingNotifyPyStart(pyFileName)
    
    def AgingNotifyPyStop(this, pyFileName) : 
        return this.__TDevice.AgingNotifyPyStop(pyFileName)

    def AgingSetCurJobInfo(this, dutIdx, jobID, status, scIdx, scCount, desc) : 
        return this.__TDevice.AgingSetCurJobInfo(dutIdx, jobID, status, scIdx, scCount, desc)

    def AgingSetCurScInfo(this, dutIdx, scID, status, tcIdx, tcCount, desc) : 
        return this.__TDevice.AgingSetCurScInfo(dutIdx, scID, status, tcIdx, tcCount, desc)

    def AgingSetCurTcInfo(this, dutIdx, tcID, status, tcStepIdx, tcStepCount, desc) : 
        return this.__TDevice.AgingSetCurTcInfo(dutIdx, tcID, status, tcStepIdx, tcStepCount, desc)

    def AgingSetCurTcStepInfo(this, dutIdx, tcStepID, status, desc) : 
        return this.__TDevice.AgingSetCurTcStepInfo(dutIdx, tcStepID, status, desc)

    def AgingMeasureADC(this, dutIdx) : 
        this.__TDevice.AgingMeasureADC(dutIdx)
        #resList = this.__TDevice.AgingMeasureADC(dutIdx)
        #if(len(resList) > 0) :
        #    this.__AgingMeasureAdcCount+=1
        #return resList

    def GetAgingMeasureADCCount(this) :
        return this.__AgingMeasureAdcCount






