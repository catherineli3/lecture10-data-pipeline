# GitHub 练习完整操作指南

本指南将帮助你完成GitHub练习的所有要求。

---

## 步骤 1: 创建GitHub仓库

### 操作步骤：

1. **访问GitHub创建页面**
   - 打开浏览器，访问：https://github.com/new

2. **填写仓库信息**
   - Repository name: `lecture10-data-pipeline` (或其他名称)
   - Description: `Data processing pipeline with GitHub Actions automation`
   - 选择 **Public** 或 **Private**
   - **重要**: ⚠️ 不要勾选任何以下选项：
     - ❌ Add a README file
     - ❌ Add .gitignore
     - ❌ Choose a license

3. **点击 "Create repository"**

---

## 步骤 2: 连接本地仓库到GitHub

创建仓库后，GitHub会显示快速设置页面。选择 "…or push an existing repository from the command line"，复制显示的命令。

### 执行以下命令（替换YOUR_USERNAME）：

```bash
cd d:/6318/lecture10-inclass-excercise

# 替换为你的GitHub用户名和仓库名
git remote add origin https://github.com/YOUR_USERNAME/lecture10-data-pipeline.git
git branch -M main
git push -u origin main
```

**示例**（假设你的用户名是`student123`）：
```bash
git remote add origin https://github.com/student123/lecture10-data-pipeline.git
git branch -M main
git push -u origin main
```

---

## 步骤 3: 验证GitHub Actions工作流触发

推送完成后：

1. **访问你的GitHub仓库**
   - 点击仓库页面顶部的 "Actions" 标签

2. **查看工作流运行**
   - 你应该看到一个工作流运行：`Data Processing Pipeline`
   - 点击查看详细日志

3. **检查工作流步骤**
   - ✅ Checkout code
   - ✅ Set up Python 3.12
   - ✅ Install dependencies
   - ✅ Run clean_and_merge script
   - ✅ Upload database as artifact
   - ✅ Commit updated database

如果所有步骤都是绿色的✅，说明工作流成功运行！

---

## 步骤 4: 故意破坏工作流并修复

### 4.1 故意破坏工作流

创建一个会失败的订单文件：

```bash
# 创建一个格式错误的订单文件
cd d:/6318/lecture10-inclass-excercise
echo "invalid,data,here" > data/orders_broken.csv
```

提交并推送：
```bash
git add data/orders_broken.csv
git commit -m "Break the workflow - invalid data format"
git push
```

**观察结果**：
- 访问GitHub Actions标签
- 工作流应该会失败（红色❌）
- 查看失败原因（可能是pandas无法解析CSV）

### 4.2 修复工作流

删除错误文件，创建正确的数据：

```bash
# 删除错误文件
rm data/orders_broken.csv

# 创建正确的数据
echo "order_id,customer_id,amount,amount_currency,order_date" > data/orders_fixed.csv
echo "16,107,150,CNY,2024-01-15" >> data/orders_fixed.csv
```

提交修复：
```bash
git add data/orders_fixed.csv
git commit -m "Fix the workflow - add valid order data"
git push
```

**观察结果**：
- 工作流应该再次成功（绿色✅）

---

## 步骤 5: 添加协作者（讲师和TA）

### 5.1 添加协作者的步骤

1. **访问仓库设置**
   - 在仓库页面，点击 "Settings" 标签

2. **找到协作者设置**
   - 在左侧菜单中找到 "Collaborators"
   - 如果是私有仓库，在 "Access" -> "Collaborators"
   - 如果是公共仓库，在 "Danger Zone" -> "Manage Access"

3. **添加协作者**
   - 点击 "Add people"
   - 输入讲师和TA的GitHub用户名
   - 选择权限级别（通常是 "Write" 或 "Admin"）
   - 点击 "Add"

### 5.2 分享仓库链接

添加协作者后，分享你的仓库链接给教学团队：

```
https://github.com/YOUR_USERNAME/lecture10-data-pipeline
```

---

## 进阶测试：触发多次工作流

### 测试1: 添加新订单

```bash
# 添加新订单
echo "17,108,200,USD,2024-01-16" >> data/orders_test.csv

# 提交并推送
git add data/orders_test.csv
git commit -m "Add new order - test workflow trigger"
git push
```

### 测试2: 添加重复订单（测试去重功能）

```bash
# 创建包含重复ID的订单
echo "1,101,50,USD,2024-01-17" >> data/orders_duplicate.csv

# 提交并推送
git add data/orders_duplicate.csv
git commit -m "Test deduplication - add duplicate order_id=1"
git push
```

### 测试3: 测试不同货币

```bash
# 添加不同货币的订单
echo "18,109,1000,JPY,2024-01-18" >> data/orders_currency.csv
echo "19,110,75,EUR,2024-01-19" >> data/orders_currency.csv

# 提交并推送
git add data/orders_currency.csv
git commit -m "Test currency conversion - JPY and EUR"
git push
```

---

## 检查工作流产物 (Artifacts)

每次工作流运行后，你可以下载更新的数据库：

1. 访问 "Actions" 标签
2. 点击任意一次工作流运行
3. 向下滚动到 "Artifacts" 部分
4. 点击 "orders-database" 下载
5. 解压后使用SQLite浏览器查看 `orders.db`

---

## 使用Flask前端查看数据

在本地启动Flask应用查看最新的数据：

```bash
cd d:/6318/lecture10-inclass-excercise
python run_app.py
```

然后在浏览器访问：http://localhost:5000

前端会每10秒自动刷新显示最新数据。

---

## 提交要求检查清单

在分享给教学团队前，确保：

- [ ] GitHub仓库已创建
- [ ] Python项目已上传
- [ ] GitHub Actions工作流已配置
- [ ] 工作流至少成功运行一次
- [ ] 工作流已故意破坏并修复
- [ ] 工作流文件有详细的注释说明
- [ ] 讲师已添加为协作者
- [ ] TA已添加为协作者
- [ ] 仓库链接已分享给教学团队

---

## 常见问题

### Q1: 推送时提示权限错误
**A**: 可能需要使用Personal Access Token (PAT):
1. Settings -> Developer settings -> Personal access tokens -> Tokens (classic)
2. 生成新token，勾选 `repo` 权限
3. 使用token代替密码进行推送

### Q2: 工作流没有触发
**A**: 检查：
1. 文件是否在 `data/` 文件夹中
2. 是否推送到了 `main` 或 `master` 分支
3. 工作流文件路径是否正确：`.github/workflows/data-pipeline.yml`

### Q3: 如何修改工作流触发条件
**A**: 编辑 `.github/workflows/data-pipeline.yml` 文件中的 `on:` 部分

---

## 项目结构总览

```
lecture10-data-pipeline/
├── .github/
│   └── workflows/
│       └── data-pipeline.yml    # GitHub Actions工作流（带详细注释）
├── data/
│   ├── customers.csv             # 客户数据
│   ├── orders.csv                # 订单数据
│   ├── orders_new.csv            # 新增订单
│   ├── orders_more.csv           # 更多订单（含重复）
│   └── orders.db                 # SQLite数据库（自动生成）
├── templates/
│   └── index.html                # Flask前端页面
├── clean_and_merge.py            # 数据处理脚本
├── app.py                        # Flask应用
├── run_app.py                    # 启动脚本
├── requirements.txt              # Python依赖
├── README.md                     # 项目说明
├── GITHUB_SETUP.md               # GitHub设置指南
└── COMPLETE_GITHUB_GUIDE.md      # 本指南
```

---

祝练习顺利！如有问题，请查看GitHub Actions日志或询问教学团队。
