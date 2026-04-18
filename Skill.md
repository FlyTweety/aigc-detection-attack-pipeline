---
name: aigc-detection-attack-pipeline
description: 对AI图像检测系统进行攻击。在用户想要攻击AI图像检测系统或者探寻AI图像检测系统弱点时进行使用。
---

# AIGC_Detectuib_Attack_Pipeline

## Description
针对AI生成图像检测方法的自动化攻击管道。主要通过对图像施加不同类型的后处理，使得AI生成图像检测方法无法正确判断图像是否是由AI生成的。

## 相关脚本说明
该skill包含以下脚本：

`scripts/get_image_path.py`: 
- 无输入参数
- 输出参数1：`image_path`，类型为`list(string)`，代表本次要处理的图像所在地址列表

`scripts/process_image_path.py`: 
- 输入参数1：`image_path`，类型为`list(string)`，代表本次要处理的图像所在地址列表；
- 输入参数2：`attack_type`，类型为`string`，代表本次处理方法，取值范围为["JPEG", "BLUR"]；
- 输出参数1：`processed_image_path`，类型为`list(string)`，代表处理后的图像所在地址；

`scripts/det_image_path.py`:
- 输出参数1：`processed_image_path`，类型为`list(string)`，代表用于检测的图像所在地址；
- 输出参数1：`aigc_det_results`，类型为`list(dict)`，代表AI输出图像检测方法所给出的检测结果；

## 工作流示例
1. 调用`scripts/get_image_path.py`获得要处理的图像地址`image_path`
2. 调用`scripts/process_image_path.py image_path attack_type`获得处理过后的图像地址`processed_image_path`
3. 调用`scripts/det_image_path.py processed_image_path`，获得针对给定图像的检测结果`aigc_det_results`