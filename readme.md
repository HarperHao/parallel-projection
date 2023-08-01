这份代码是计算机图形学的结课作业。实现了将大卫雕像三维模型平行投影到二维物体的过程。
流程：三维点云->二维点云->三角网格实体化->网格阈值裁剪

## Prepare

* 使用VisualSFM和MeshLab导出三维模型.ply文件
* 使用编译器：Matlab2020a+Python3.8
* 准备Python所需要包: pip install -r requirements.txt

## How to run this project

1. run ply2txt.m，将.ply中三维点云点导到.txt文件中
2. run projection.py 三维点云平行投影到二维点云。根据三维点云数据分别得到x0y,x0z,yoz平面二维点云数据，并保存到指定的txt文件中
3. run truangulation.py 对二维点云进行三角网格化。传入第2步得到的二维点云txt文件，输出其三角网格化后的结果。
4. run prune.py 对三角网格进行阈值裁剪。设定不同的area_threshold对网格进行裁剪。
5. run utils.py 对保存下的yoz平面投影的二维物体图片执行旋转和添加图例操作。