1、分类器选择:
lr/gbdt/fm/mlp
2、特征设计与挖掘
设想综合利用特征集成和模型集成,想到fm有特征embedding的作用
组露出优选模型中最终的是挖掘出同组文章之间的差异特征
3、数据介绍:
组露出优选的标注标准是,针对同组文章,露出文章标注为1,其他为0.
想法:
A、同组同维度特征进行归一化可以体现同组之前的差异
B、特征维度设计: