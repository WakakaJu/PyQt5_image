# PyQt5_image
基于PyQt5开发的图像处理图形用户界面</br>
包含的文件：</br>
`image_processing.ui`是由Qtdesigner设计得到的界面模板</br>
`image_processing.py`是由`image_processing.ui`转化而来的代码文件，其中包含了`.ui`设计的布局，以及后续添加的功能和方法函数</br>
`main.py`是图形界面运行的主函数。如后期需要另外添加功能，直接写在配置文件`image_processing.py`中即可，主函数文件`main.py`不必改动。</br>
**github里图片没法改大小，看着有点别扭，可以下载pdf文档看**
</br></br>
本项目是基于PyQt5开发的图形用户界面，可实现三个功能：**图像分割、图像增强、边缘检测**。</br>
使用designer软件设计界面构成，设计三个单选功能按钮（图像分割、图像增强、边缘检测），每个功能按钮下链接四个多选按钮，用于实现功能下不同的方法和参数，更好对比效果。每个功能下的多选按钮与功能按钮单独对应。</br>
**图像分割**可选择：OTSU法（大津法）、最大熵分割法、迭代阈值分割法、马尔可夫随机场法(其中，由于马尔可夫随机场特殊的分类特性，默认将图像分割成四类)：</br>
![img_pro1](https://user-images.githubusercontent.com/88924975/170828254-a5f3c1fe-6753-491f-8c41-ff487ed22182.png)</br></br>

**图像增强**可选择：标准直方图均衡(HE)、限制对比度自适应直方图均衡(CLAHE)、单尺度Retinex算法(SSR)、多尺度Retinex算法(MSR)： </br>
![img_pro2](https://user-images.githubusercontent.com/88924975/170828520-fc717692-b601-4d01-b5dc-ed8c2406eadf.png)</br></br>

**边缘检测**可选择：Roberts算子、Sobel算子、Canny算子、Laplacian算子：</br>
![img_pro3](https://user-images.githubusercontent.com/88924975/170828530-5cf048eb-b60c-47a2-bab9-4d930f827c3c.png)</br>

另外，还设计有选择文件按钮和开始按钮，便于用户直接操作。</br>
</br>
用户可直接通过鼠标点击的方法实现上述功能及对应方法，并进行对比。以Lena图为例，实现效果如下：</br>
**图像分割效果：**</br>
![img_pro4](https://user-images.githubusercontent.com/88924975/170828536-94dcdc71-62d6-4957-96a2-cafcbe0badd8.png)</br></br>

**图像增强效果：**</br>
![img_pro5](https://user-images.githubusercontent.com/88924975/170828545-006be88d-b643-4d93-9cc2-eb12017b8cf3.png)</br></br>

**边缘检测效果：**</br>
![img_pro6](https://user-images.githubusercontent.com/88924975/170828556-81a7dafb-c6d4-44ae-a757-ed97fab19599.png)</br>

</br>
此外，我还用我自己拍摄的我家小区的夜景效果演示一下夜景图像增强的效果:</br>

**原图**：</br>
![img_pro7](https://user-images.githubusercontent.com/88924975/170828560-20ba93b3-a3af-4311-9c3d-fe5b83541229.png)</br></br>

**增强后效果**：</br>
![img_pro8](https://user-images.githubusercontent.com/88924975/170828568-c7d3714a-e1b5-4ef0-862d-95939de50932.png)</br></br>

由于夜景图像较为特殊，在此不做图像分割和边缘检测的演示。</br></br>
*另，各方法效果对比在此不做分析，可见实验报告[《图像分割各经典方法的对比研究实验报告》](https://github.com/WakakaJu/Computer-Vision/tree/main/%E5%9B%BE%E5%83%8F%E5%88%86%E5%89%B2)及[《图像增强各经典方法的对比研究实验报告》](https://github.com/WakakaJu/Computer-Vision/tree/main/%E5%9B%BE%E5%83%8F%E5%A2%9E%E5%BC%BA)*</br></br>
***ps**：我没有把程序打包成`.exe`文件，`image_processing.py`就是整个图形界面布局和功能的配置函数，由主函数`main.py`运行，因此可以在我这个项目的基础上根据需求做任意添改。希望可以对你有所帮助*</br>
</br>
</br>
</br>
