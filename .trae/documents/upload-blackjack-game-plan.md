# 计划：将21点游戏上传到 GitHub 仓库

## 概述
将本地 `h:/Git/21点游戏/` 中的21点(Blackjack)游戏上传到 GitHub 仓库 `Chinagod88/coommon`，存入 `blackjack/` 子文件夹中，并清空仓库原有内容。

## 当前状态分析
- **本地源文件**: `h:/Git/21点游戏/`
  - `Dm.py` — 21点游戏核心代码（Python实现，约144行）
  - `规则` — 游戏规则说明文档（中文）
- **目标仓库**: `https://github.com/Chinagod88/coommon.git`（尚未克隆到本地）
- **gh CLI**: 已安装但尚未完成 GitHub 认证

## 实施步骤

### 步骤 1：配置 gh CLI 认证
- **操作**: 运行 `gh auth login` 进行交互式登录
- **说明**: 用户需要完成 GitHub 账号认证，这是后续所有操作的前提
- **验证**: `gh auth status` 确认认证成功

### 步骤 2：克隆目标仓库
- **操作**: 
  ```bash
  cd h:/Git
  gh repo clone Chinagod88/coommon
  ```
- **结果**: 仓库被克隆到 `h:/Git/coommon/`

### 步骤 3：清空仓库原有内容（保留 .git）
- **操作**: 
  ```bash
  cd h:/Git/coommon
  git rm -rf .  # 移除所有跟踪的文件
  ```
- **说明**: 清空仓库现有内容，为上传游戏文件做准备

### 步骤 4：创建 blackjack 子文件夹并复制游戏文件
- **操作**:
  ```powershell
  # 创建子文件夹
  mkdir h:/Git/coommon/blackjack
  
  # 复制游戏文件
  Copy-Item "h:/Git/21点游戏/Dm.py" "h:/Git/coommon/blackjack/Dm.py"
  Copy-Item "h:/Git/21点游戏/规则" "h:/Git/coommon/blackjack/规则"
  ```
- **结果**: 仓库目录结构为：
  ```
  coommon/
  └── blackjack/
      ├── Dm.py
      └── 规则
  ```

### 步骤 5：提交并推送到 GitHub
- **操作**:
  ```bash
  cd h:/Git/coommon
  git add .
  git commit -m "Add blackjack game"
  git push origin main
  ```
- **说明**: 提交信息为英文 "Add blackjack game"

## 假设与决策
| 决策 | 选择 |
|------|------|
| 目标文件夹 | `blackjack/`（用户指定） |
| 提交语言 | 英文（用户指定） |
| 原有内容处理 | 清空后上传（用户指定） |
| gh CLI 认证 | 未认证，需要首次设置（用户确认） |

## 验证方式
1. `gh auth status` — 确认认证状态
2. `git status` — 确认文件已正确暂存
3. `git log --oneline` — 确认提交记录
4. 在浏览器中访问 `https://github.com/Chinagod88/coommon` 确认文件已上传