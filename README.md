# Python 数据处理 — 实验01 与 作业01

| 项目 | 内容 |
|---|---|
| 课程 | Python 数据处理 |
| 任务 | 第一个任务（实验 EXP01 + 作业 HW01） |
| 学号 | 20244630202 |
| 姓名 | 赵怡然 |

## 目录结构

```
.
├── 20244630202_赵怡然_exp01.ipynb     实验：Python 基础与数据处理入门
├── 20244630202_赵怡然_hw01.ipynb      作业：Data Types, Functions and Conditionals
├── student_utils.py                   实验4 任务7 要求的解析模块（必须保留）
├── exp01_data/                        实验4 由程序自动生成的数据目录
│   ├── students.txt
│   ├── report.txt
│   ├── students.pkl
│   └── mode_demo.txt
├── .gitignore
└── README.md
```

## 运行环境

| 项目 | 版本 / 说明 |
|---|---|
| conda 环境 | `exp_env`（独立环境，未使用 base） |
| Python | 3.11.17 |
| Jupyter | notebook 7.6.3、jupyterlab 4.6.4 |
| 内核 | `exp01`，显示名 `Python 3.11 (exp_env)` |
| 其他库 | numpy 2.4.6、pandas 3.0.6、matplotlib 3.11.1 |

环境复现命令：

```bash
conda create -n exp_env python=3.11 -y
conda activate exp_env
conda install -y jupyter ipykernel numpy pandas matplotlib
python -m ipykernel install --user --name exp01 --display-name "Python 3.11 (exp_env)"
```

## 如何运行

1. 启动 Jupyter：先 `conda activate exp_env`，再执行 `jupyter notebook`
2. 打开 `20244630202_赵怡然_exp01.ipynb`，右上角内核选择 **Python 3.11 (exp_env)**
3. 菜单 **Kernel → Restart Kernel and Run All Cells**，从头到尾顺序运行
4. 作业 `20244630202_赵怡然_hw01.ipynb` 同样操作

## 两点说明

1. 实验4 任务1 用的是 `os.path.join(os.getcwd(), "exp01_data")`，所以 `exp01_data/` 会创建在 **notebook 所在的目录** 下。请保持本文件与两个 notebook 在同一层。
2. `exp01_data/` 特意**没有**写进 `.gitignore`，这样实验的产出物会随仓库一起保存。`students.txt` 以 UTF-8 写入，Windows 上换行是 CRLF，Python 读取时会自动还原，不影响按行解析。