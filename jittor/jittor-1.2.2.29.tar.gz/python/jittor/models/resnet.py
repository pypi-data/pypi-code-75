# ***************************************************************
# Copyright (c) 2021 Jittor. All Rights Reserved. 
# Maintainers: 
#     Guowei Yang <471184555@qq.com>
#     Wenyang Zhou <576825820@qq.com>
#     Dun Liang <randonlang@gmail.com>. 
# 
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.
# ***************************************************************
# This model is generated by pytorch converter.
import jittor as jt
from jittor import nn

__all__ = ['ResNet', 'Resnet18', 'Resnet34', 'Resnet26', 'Resnet38', 'Resnet50', 'Resnet101', 'Resnet152', 'Resnext50_32x4d', 'Resnext101_32x8d', 'Wide_resnet50_2', 'Wide_resnet101_2',
    'resnet18', 'resnet34', 'resnet26', 'resnet38', 'resnet50', 'resnet101', 'resnet152', 'resnext50_32x4d', 'resnext101_32x8d', 'wide_resnet50_2', 'wide_resnet101_2']

def conv3x3(in_planes, out_planes, stride=1, groups=1, dilation=1):
    conv=nn.Conv(in_planes, out_planes, kernel_size=3, stride=stride, padding=dilation, groups=groups, bias=False, dilation=dilation)
    jt.init.relu_invariant_gauss_(conv.weight, mode="fan_out")
    return conv

def conv1x1(in_planes, out_planes, stride=1):
    conv=nn.Conv(in_planes, out_planes, kernel_size=1, stride=stride, bias=False)
    jt.init.relu_invariant_gauss_(conv.weight, mode="fan_out")
    return conv

class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, inplanes, planes, stride=1, downsample=None, groups=1, base_width=64, dilation=1, norm_layer=None):
        super(BasicBlock, self).__init__()
        if (norm_layer is None):
            norm_layer = nn.BatchNorm
        if ((groups != 1) or (base_width != 64)):
            raise ValueError('BasicBlock only supports groups=1 and base_width=64')
        if (dilation > 1):
            raise NotImplementedError('Dilation > 1 not supported in BasicBlock')
        self.conv1 = conv3x3(inplanes, planes, stride)
        self.bn1 = norm_layer(planes)
        self.relu = nn.Relu()
        self.conv2 = conv3x3(planes, planes)
        self.bn2 = norm_layer(planes)
        self.downsample = downsample
        self.stride = stride

    def execute(self, x):
        identity = x
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)
        out = self.conv2(out)
        out = self.bn2(out)
        if (self.downsample is not None):
            identity = self.downsample(x)
        out += identity
        out = self.relu(out)
        return out

class Bottleneck(nn.Module):
    expansion = 4

    def __init__(self, inplanes, planes, stride=1, downsample=None, groups=1, base_width=64, dilation=1, norm_layer=None):
        super(Bottleneck, self).__init__()
        if (norm_layer is None):
            norm_layer = nn.BatchNorm
        width = (int((planes * (base_width / 64.0))) * groups)
        self.conv1 = conv1x1(inplanes, width)
        self.bn1 = norm_layer(width)
        self.conv2 = conv3x3(width, width, stride, groups, dilation)
        self.bn2 = norm_layer(width)
        self.conv3 = conv1x1(width, (planes * self.expansion))
        self.bn3 = norm_layer((planes * self.expansion))
        self.relu = nn.Relu()
        self.downsample = downsample
        self.stride = stride

    def execute(self, x):
        identity = x
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)
        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu(out)
        out = self.conv3(out)
        out = self.bn3(out)
        if (self.downsample is not None):
            identity = self.downsample(x)
        out += identity
        out = self.relu(out)
        return out

class ResNet(nn.Module):

    def __init__(self, block, layers, num_classes=1000, zero_init_residual=False, groups=1, width_per_group=64, replace_stride_with_dilation=None, norm_layer=None):
        super(ResNet, self).__init__()
        if (norm_layer is None):
            norm_layer = nn.BatchNorm
        self._norm_layer = norm_layer
        self.inplanes = 64
        self.dilation = 1
        if (replace_stride_with_dilation is None):
            replace_stride_with_dilation = [False, False, False]
        if (len(replace_stride_with_dilation) != 3):
            raise ValueError('replace_stride_with_dilation should be None or a 3-element tuple, got {}'.format(replace_stride_with_dilation))
        self.groups = groups
        self.base_width = width_per_group
        self.conv1 = nn.Conv(3, self.inplanes, kernel_size=7, stride=2, padding=3, bias=False)
        jt.init.relu_invariant_gauss_(self.conv1.weight, mode="fan_out")
        self.bn1 = norm_layer(self.inplanes)
        self.relu = nn.Relu()
        self.maxpool = nn.Pool(kernel_size=3, stride=2, padding=1, op='maximum')
        self.layer1 = self._make_layer(block, 64, layers[0])
        self.layer2 = self._make_layer(block, 128, layers[1], stride=2, dilate=replace_stride_with_dilation[0])
        self.layer3 = self._make_layer(block, 256, layers[2], stride=2, dilate=replace_stride_with_dilation[1])
        self.layer4 = self._make_layer(block, 512, layers[3], stride=2, dilate=replace_stride_with_dilation[2])
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear((512 * block.expansion), num_classes)

    def _make_layer(self, block, planes, blocks, stride=1, dilate=False):
        norm_layer = self._norm_layer
        downsample = None
        previous_dilation = self.dilation
        if dilate:
            self.dilation *= stride
            stride = 1
        if ((stride != 1) or (self.inplanes != (planes * block.expansion))):
            downsample = nn.Sequential(conv1x1(self.inplanes, (planes * block.expansion), stride), norm_layer((planes * block.expansion)))
        layers = []
        layers.append(block(self.inplanes, planes, stride, downsample, self.groups, self.base_width, previous_dilation, norm_layer))
        self.inplanes = (planes * block.expansion)
        for _ in range(1, blocks):
            layers.append(block(self.inplanes, planes, groups=self.groups, base_width=self.base_width, dilation=self.dilation, norm_layer=norm_layer))
        return nn.Sequential(*layers)

    def _forward_impl(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.avgpool(x)
        x = jt.reshape(x, (x.shape[0], -1))
        x = self.fc(x)
        return x

    def execute(self, x):
        return self._forward_impl(x)

def _resnet(block, layers, **kwargs):
    model = ResNet(block, layers, **kwargs)
    return model

def Resnet18(pretrained=False, **kwargs):
    model = _resnet(BasicBlock, [2, 2, 2, 2], **kwargs)
    if pretrained: model.load("jittorhub://resnet18.pkl")
    return model
resnet18 = Resnet18

def Resnet34(pretrained=False, **kwargs):
    model = _resnet(BasicBlock, [3, 4, 6, 3], **kwargs)
    if pretrained: model.load("jittorhub://resnet34.pkl")
    return model
resnet34 = Resnet34

def Resnet50(pretrained=False, **kwargs):
    model = _resnet(Bottleneck, [3, 4, 6, 3], **kwargs)
    if pretrained: model.load("jittorhub://resnet50.pkl")
    return model

resnet50 = Resnet50

def Resnet38(**kwargs):
    return _resnet(Bottleneck, [2, 3, 5, 2], **kwargs)
resnet38 = Resnet38

def Resnet26(**kwargs):
    return _resnet(Bottleneck, [1, 2, 4, 1], **kwargs)
resnet26 = Resnet26

def Resnet101(pretrained=False, **kwargs):
    """
    ResNet-101 model architecture.

    Example::

        model = jittor.models.Resnet101()
        x = jittor.random([10,224,224,3])
        y = model(x) # [10, 1000]

    """
    model = _resnet(Bottleneck, [3, 4, 23, 3], **kwargs)
    if pretrained: model.load("jittorhub://resnet101.pkl")
    return model
resnet101 = Resnet101

def Resnet152(pretrained=False, **kwargs):
    model = _resnet(Bottleneck, [3, 8, 36, 3], **kwargs)
    if pretrained: model.load("jittorhub://resnet152.pkl")
    return model
resnet152 = Resnet152

def Resnext50_32x4d(pretrained=False, **kwargs):
    kwargs['groups'] = 32
    kwargs['width_per_group'] = 4
    model = _resnet(Bottleneck, [3, 4, 6, 3], **kwargs)
    if pretrained: model.load("jittorhub://resnext50_32x4d.pkl")
    return model
resnext50_32x4d = Resnext50_32x4d

def Resnext101_32x8d(pretrained=False, **kwargs):
    kwargs['groups'] = 32
    kwargs['width_per_group'] = 8
    model = _resnet(Bottleneck, [3, 4, 23, 3], **kwargs)
    if pretrained: model.load("jittorhub://resnext101_32x8d.pkl")
    return model
resnext101_32x8d = Resnext101_32x8d

def Wide_resnet50_2(pretrained=False, **kwargs):
    kwargs['width_per_group'] = (64 * 2)
    model = _resnet(Bottleneck, [3, 4, 6, 3], **kwargs)
    if pretrained: model.load("jittorhub://wide_resnet50_2.pkl")
    return model
wide_resnet50_2 = Wide_resnet50_2

def Wide_resnet101_2(pretrained=False, **kwargs):
    kwargs['width_per_group'] = (64 * 2)
    model = _resnet(Bottleneck, [3, 4, 23, 3], **kwargs)
    if pretrained: model.load("jittorhub://wide_resnet101_2.pkl")
    return model
wide_resnet101_2 = Wide_resnet101_2