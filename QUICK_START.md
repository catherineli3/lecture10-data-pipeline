# GitHub 练习快速开始卡片

## 📋 练习要求完成情况

| 要求 | 状态 | 说明 |
|------|------|------|
| ✅ 创建GitHub仓库 | ⏳ 待执行 | 需要手动在GitHub网站创建 |
| ✅ 上传Python项目 | ⏳ 待执行 | 需要连接远程仓库并推送 |
| ✅ GitHub Actions工作流 | ✅ 已完成 | `.github/workflows/data-pipeline.yml` |
| ✅ 详细注释 | ✅ 已完成 | 工作流包含详细中文注释 |
| ✅ 故意破坏并修复 | ⏳ 待执行 | 在推送后执行测试 |
| ✅ 添加协作者 | ⏳ 待执行 | 在GitHub仓库设置中添加 |

---

## 🚀 快速开始（3步）

### 第1步：创建GitHub仓库
1. 访问：https://github.com/new
2. 仓库名：`lecture10-data-pipeline`
3. 不要勾选README等选项
4. 点击创建

### 第2步：连接并推送（替换YOUR_USERNAME）
```bash
git remote add origin https://github.com/YOUR_USERNAME/lecture10-data-pipeline.git
git branch -M main
git push -u origin main
```

### 第3步：验证工作流
1. 访问GitHub仓库的 "Actions" 标签
2. 查看工作流运行状态
3. 应该看到所有步骤都是绿色✅

---

## 🎯 后续测试步骤

### 测试破坏工作流
```bash
# 创建错误数据
echo "invalid,data,here" > data/orders_broken.csv
git add data/orders_broken.csv
git commit -m "Break workflow - invalid data"
git push
```

### 修复工作流
```bash
# 删除错误文件，创建正确数据
rm data/orders_broken.csv
echo "order_id,customer_id,amount,amount_currency,order_date" > data/orders_fixed.csv
echo "16,107,150,CNY,2024-01-15" >> data/orders_fixed.csv
git add data/orders_fixed.csv
git commit -m "Fix workflow - valid data"
git push
```

### 添加更多测试数据
```bash
# 新订单
echo "17,108,200,USD,2024-01-16" >> data/orders_test.csv
git add data/orders_test.csv
git commit -m "Add new order"
git push
```

---

## 👥 添加协作者

1. 访问仓库 -> Settings -> Collaborators (或 Manage Access)
2. 点击 "Add people"
3. 输入讲师和TA的GitHub用户名
4. 选择权限（Write或Admin）
5. 点击 "Add"

---

## 📊 当前项目统计

- 📁 15个唯一订单
- 🏢 4个区域（North, South, East, West）
- 💰 3种货币（USD, EUR, CNY, JPY）
- 🔧 6个GitHub Actions步骤
- 📄 1个SQLite数据库
- 🌐 1个Flask Web应用

---

## 🔍 查看详细指南

完整指南请查看：`COMPLETE_GITHUB_GUIDE.md`

---

## 💡 提示

- 所有命令都在项目目录执行：`d:/6318/lecture10-inclass-excercise`
- GitHub Actions会在 `data/` 文件夹变化时自动触发
- 前端应用：`python run_app.py` 访问 http://localhost:5000
- 查看提交历史：`git log --oneline`

---

## ✅ 完成检查清单

- [ ] 在GitHub创建仓库
- [ ] 推送代码到GitHub
- [ ] Actions工作流成功运行
- [ ] 故意破坏工作流（看到失败❌）
- [ ] 修复工作流（看到成功✅）
- [ ] 添加讲师为协作者
- [ ] 添加TA为协作者
- [ ] 分享仓库链接给教学团队

---

**准备好开始了吗？请告诉我你的GitHub用户名，我可以帮你准备完整的推送命令！**
