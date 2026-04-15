# 智能风电功率预测平台

![Platform Preview](https://img.shields.io/badge/Platform-Wind%20Power%20Prediction-blue.svg)
![Tech Stack](https://img.shields.io/badge/Tech-HTML5%20%7C%20CSS3%20%7C%20JavaScript-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

基于深度学习的风电场功率预测与智能管理可视化平台

## ✨ 功能特性

- 🌡️ **实时监控仪表盘** - 温度、风速实时监测
- 📊 **功率预测图表** - 交互式折线图，支持鼠标悬停查看数据
- 📈 **数据分析模块** - 发电量排名、统计分析，支持时间范围切换
- 📍 **定点预测** - 未来24小时功率与风速预测
- 🎛️ **风机管理** - 设备信息、运行参数、告警历史监控
- 📦 **模型导入** - 支持 HDF5、SavedModel、PyTorch 格式
- 📥 **数据导入** - CSV 格式数据文件上传

## 🚀 快速开始

### 方式一：直接打开（推荐）

```bash
# 双击打开即可，无需安装依赖
wind_power_dashboard.html
```

### 方式二：启动本地服务器

```bash
# 安装依赖
pip install -r requirements.txt

# 启动服务器
python start_server.py

# 访问页面
# http://localhost:8888
```

## 📁 项目结构

```
power_load_prediction/
├── wind_power_dashboard.html    # 主页面 - 智能风电功率预测平台
├── templates/
│   └── index.html              # Flask模板页面
├── src/                        # Python源代码目录
│   ├── data_preprocessing.py   # 数据预处理
│   ├── model.py                # LSTM模型构建
│   ├── train.py                # 训练脚本
│   ├── predict.py              # 预测模块
│   └── visualization.py        # 可视化模块
├── data/                       # 数据目录
├── models/                     # 模型保存目录
├── start_server.py             # HTTP服务器启动脚本
├── config.py                   # 配置文件
├── requirements.txt            # Python依赖清单
└── README.md                   # 项目说明文档
```

## 🛠️ 技术栈

| 分类 | 技术 | 版本 |
|------|------|------|
| 前端框架 | HTML5 | - |
| 样式 | CSS3 | - |
| 脚本 | JavaScript ES6+ | - |
| 图表库 | Chart.js | 3.x |
| 后端 | Python Flask | 2.x |
| 深度学习 | TensorFlow / PyTorch | - |

## 📊 功能模块详解

### 1. 功率预测
- 实时温度仪表盘
- 实时风速仪表盘
- 功率趋势折线图（支持切换功率/趋势模式）
- 风机负载分布柱状图

### 2. 数据分析
- 平均功率统计
- 平均气温/风速/气压/湿度统计
- 发电功率历史排名表格
- 支持近一周/近一月/近一年数据切换

### 3. 定点预测
- 未来24小时功率预测曲线
- 功率与风速双轴对比图

### 4. 风机管理
- 风机设备信息展示
- 运行参数实时监控
- 历史告警信息表格
- 支持多风机切换

### 5. 导入功能
- 模型权重导入（支持 .h5, .pb, .pt 格式）
- 数据文件导入（支持 .csv 格式）

## 📱 响应式设计

- 支持桌面端和移动端访问
- 自适应布局，自动调整显示效果

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 📧 联系方式

如有问题或建议，请通过 Issue 联系。