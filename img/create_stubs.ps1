# 关卡数据定义
$levels = @(
  @{
    file = "train.md"
    title = "🚂 第二关：火车 (Train)"
    desc = "人类一败涂地火车关卡攻略"
    difficulty = "⭐⭐☆☆☆"
    duration = "12 分钟"
    weight = 3
    image = "/img/climbing.jpg"
    tip = "利用车厢顶上的缝隙和边缘攀爬，可以直接跨越阻挡门，省去去拉闸解谜的繁琐步骤。"
  },
  @{
    file = "carry.md"
    title = "📦 第三关：搬运 (Carry)"
    desc = "人类一败涂地搬运关卡攻略"
    difficulty = "⭐⭐☆☆☆"
    duration = "10 分钟"
    weight = 4
    image = "/img/factory.jpg"
    tip = "使用双手反向推拉大箱子做掩体，在跳跃时抓取最高边缘，可以直接抓跳跨过大部分高栏。"
  },
  @{
    file = "mountain.md"
    title = "⛰️ 第四关：山巅 (Mountain)"
    desc = "人类一败涂地山巅关卡攻略"
    difficulty = "⭐⭐⭐☆☆"
    duration = "20 分钟"
    weight = 5
    image = "/img/climbing.jpg"
    tip = "爬山时面向山壁双手抓取，然后有节奏地使用“左右摆头”触发单手高抓判定，可以直接跨越陡峭断崖。"
  },
  @{
    file = "demolition.md"
    title = "🏗️ 第五关：拆除 (Demolition)"
    desc = "人类一败涂地拆除关卡攻略"
    difficulty = "⭐⭐⭐☆☆"
    duration = "18 分钟"
    weight = 6
    image = "/img/swinging.jpg"
    tip = "抱起铁球并用力向玻璃窗甩动甩飞，可以大幅缩短撞击玻璃窗的次数，或者直接跳在废弃铁架上翻墙。"
  },
  @{
    file = "castle.md"
    title = "🏰 第六关：城堡 (Castle)"
    desc = "人类一败涂地城堡关卡攻略"
    difficulty = "⭐⭐⭐☆☆"
    duration = "25 分钟"
    weight = 7
    image = "/img/climbing.jpg"
    tip = "使用投石车时，可以把自己放在投石机勺子里拉下拉杆，利用重力加速度把自己直接发射到城堡最深处。"
  },
  @{
    file = "water.md"
    title = "⛵ 第七关：水 (Water)"
    desc = "人类一败涂地水关卡攻略"
    difficulty = "⭐⭐⭐☆☆"
    duration = "25 分钟"
    weight = 8
    image = "/img/multiplayer.jpg"
    tip = "驾驶摩托艇转弯时松开手柄反向移动，可以做出漂移掉头动作；水下螺旋桨反冲起跳可以飞过高坡。"
  },
  @{
    file = "power.md"
    title = "⚡ 第八关：动力 (Power)"
    desc = "人类一败涂地动力关卡攻略"
    difficulty = "⭐⭐⭐☆☆"
    duration = "30 分钟"
    weight = 9
    image = "/img/factory.jpg"
    tip = "把电池接线接在备用电路板的同极接口可以触发短路火花，或者拉住发电风扇风叶直接荡到对岸阳台。"
  },
  @{
    file = "aztec.md"
    title = "🗿 第九关：阿兹特克 (Aztec)"
    desc = "人类一败涂地阿兹特克关卡攻略"
    difficulty = "⭐⭐⭐⭐☆"
    duration = "30 分钟"
    weight = 10
    image = "/img/mansion.jpg"
    tip = "在大石球滚下时，跳起反向抓住滚动的石球，可以利用石球的切线速度直接把自己甩上终点桥头。"
  },
  @{
    file = "dark.md"
    title = "🌃 第十关：黑暗 (Dark)"
    desc = "人类一败涂地黑暗关卡攻略"
    difficulty = "⭐⭐⭐⭐☆"
    duration = "30 分钟"
    weight = 11
    image = "/img/cover.jpg"
    tip = "将红蓝两线接入变电箱之后，拉出备用发电机插头挂在滑轮索上，像飞索一样直接滑向后院出口。"
  },
  @{
    file = "steam.md"
    title = "💨 第十一关：蒸汽 (Steam)"
    desc = "人类一败涂地蒸汽关卡攻略"
    difficulty = "⭐⭐⭐☆☆"
    duration = "30 分钟"
    weight = 12
    image = "/img/swinging.jpg"
    tip = "踩在高压蒸汽喷口上，在喷口爆出气流的瞬间起跳，可以被高压气流托起，瞬间飞上5米高的铁管通道。"
  },
  @{
    file = "ice.md"
    title = "❄️ 第十二关：冰 (Ice)"
    desc = "人类一败涂地冰关卡攻略"
    difficulty = "⭐⭐⭐☆☆"
    duration = "25 分钟"
    weight = 13
    image = "/img/cover.jpg"
    tip = "将木板架在冰面斜坡，用身体做阻尼下滑，能在到达断崖前获得双倍的跳跃初速度。"
  },
  @{
    file = "thermal.md"
    title = "🌋 第十三关：热能 (Thermal)"
    desc = "人类一败涂地热能关卡攻略"
    difficulty = "⭐⭐⭐⭐☆"
    duration = "35 分钟"
    weight = 14
    image = "/img/swinging.jpg"
    tip = "抓住热气球的底边横杆，在热气球起飞到达最顶点时，侧向摆动身体放手，能直接飘落至大矿洞终点。"
  },
  @{
    file = "golf.md"
    title = "⛳ 第十五关：高尔夫 (Golf)"
    desc = "人类一败涂地高尔夫关卡攻略"
    difficulty = "⭐⭐⭐☆☆"
    duration = "25 分钟"
    weight = 16 # Factory is 15 (weight=2), actually Mansion=1, Factory=2, but we will make weights follow order
    image = "/img/multiplayer.jpg"
    tip = "推高尔夫球时，可以直接把 Bob 挂在杆子上用身体做重力钟摆，以大力抽击将球一杆推入超远草坪洞口。"
  },
  @{
    file = "city.md"
    title = "🏙️ 第十六关：城市 (City)"
    desc = "人类一败涂地城市关卡攻略"
    difficulty = "⭐⭐⭐⭐☆"
    duration = "30 分钟"
    weight = 17
    image = "/img/hero_banner.jpg"
    tip = "利用弹簧床的连续回弹力，在起落第三次（振幅最大时）起跳，可以直接跳上楼顶停机坪。"
  },
  @{
    file = "forest.md"
    title = "🌲 第十七关：森林 (Forest)"
    desc = "人类一败涂地森林关卡攻略"
    difficulty = "⭐⭐⭐⭐☆"
    duration = "35 分钟"
    weight = 18
    image = "/img/climbing.jpg"
    tip = "砍伐树木让其倾倒在悬崖之间做木桥；也可以用绳索套住木桩做钟摆动作飞跃大深渊。"
  },
  @{
    file = "laboratory.md"
    title = "🔬 第十八关：实验室 (Laboratory)"
    desc = "人类一败涂地实验室关卡攻略"
    difficulty = "⭐⭐⭐⭐☆"
    duration = "30 分钟"
    weight = 19
    image = "/img/factory.jpg"
    tip = "使用电磁磁铁吸附铁质小球做吊篮，在通电的一瞬间起跳，能利用电磁斥力将自己弹射上高空管道。"
  },
  @{
    file = "lumber.md"
    title = "🪵 第十九关：木材 (Lumber)"
    desc = "人类一败涂地木材关卡攻略"
    difficulty = "⭐⭐⭐⭐☆"
    duration = "35 分钟"
    weight = 20
    image = "/img/factory.jpg"
    tip = "将多根木头扎在一起做木筏，在激流上操纵木桨保持中心平稳，可直接漂流穿过激流险滩。"
  },
  @{
    file = "red-rock.md"
    title = "🏜️ 第二十关：红石 (Red Rock)"
    desc = "人类一败涂地红石关卡攻略"
    difficulty = "⭐⭐⭐⭐☆"
    duration = "30 分钟"
    weight = 21
    image = "/img/mansion.jpg"
    tip = "利用风扇产生的气流配合滑翔翼，可以实现长距离滑空，直接掠过大峡谷地带。"
  },
  @{
    file = "tower.md"
    title = "🗼 第二十一关：高塔 (Tower)"
    desc = "人类一败涂地高塔关卡攻略"
    difficulty = "⭐⭐⭐⭐☆"
    duration = "35 分钟"
    weight = 22
    image = "/img/climbing.jpg"
    tip = "攀爬旋转的塔壁齿轮时，顺着齿轮旋转方向顺风起跳，可以被齿轮的切向力推飞至对面水管。"
  },
  @{
    file = "miniature.md"
    title = "🔍 第二十二关：微观 (Miniature)"
    desc = "人类一败涂地微观关卡攻略"
    difficulty = "⭐⭐⭐☆☆"
    duration = "25 分钟"
    weight = 23
    image = "/img/hero_banner.jpg"
    tip = "在巨型微波炉和玩具车之间，踩在玩具车的后备箱起跳，可以利用小车的碰撞箱直接飞上桌面。"
  },
  @{
    file = "copper-world.md"
    title = "🪙 第二十三关：铜世界 (Copper World)"
    desc = "人类一败涂地铜世界关卡攻略"
    difficulty = "⭐⭐⭐⭐☆"
    duration = "35 分钟"
    weight = 24
    image = "/img/factory.jpg"
    tip = "操作巨大的电磁铁电磁吊臂，直接将电池吸附在高空中投掷进卡槽，无需费力去拉配电闸。"
  },
  @{
    file = "port.md"
    title = "⚓ 第二十四关：港口 (Port)"
    desc = "人类一败涂地港口关卡攻略"
    difficulty = "⭐⭐⭐⭐☆"
    duration = "30 分钟"
    weight = 25
    image = "/img/mansion.jpg"
    tip = "利用起重吊钩将货轮拉近码头，跳在货轮搬运工的桅杆上直接荡向对岸灯塔，可略去繁复的集装箱搬运。"
  },
  @{
    file = "underwater.md"
    title = "🐳 第二十五关：水下 (Underwater)"
    desc = "人类一败涂地水下关卡攻略"
    difficulty = "⭐⭐⭐⭐☆"
    duration = "35 分钟"
    weight = 26
    image = "/img/multiplayer.jpg"
    tip = "潜水时双手抓住潜水器侧翼，利用水下螺旋桨的反冲力，可以直接冲破海底脆弱的玻璃围板。"
  },
  @{
    file = "hike.md"
    title = "🥾 第二十六关：徒步 (Hike)"
    desc = "人类一败涂地徒步关卡攻略"
    difficulty = "⭐⭐⭐☆☆"
    duration = "25 分钟"
    weight = 27
    image = "/img/climbing.jpg"
    tip = "利用松动的巨石作为翘翘板，把箱子放在一端，自己从高处跳下踩另一端，可将箱子弹射上悬崖。"
  },
  @{
    file = "test-chamber.md"
    title = "🧬 第二十七关：测试室 (Test Chamber)"
    desc = "人类一败涂地测试室关卡攻略"
    difficulty = "⭐⭐⭐⭐☆"
    duration = "30 分钟"
    weight = 28
    image = "/img/factory.jpg"
    tip = "利用重力颠倒装置，在重力反转瞬间双手抓取天花板边缘，可以顺移直接滑入终点房。"
  },
  @{
    file = "candyland.md"
    title = "🍭 第二十八关：糖果乐园 (Candyland)"
    desc = "人类一败涂地糖果乐园关卡攻略"
    difficulty = "⭐⭐⭐☆☆"
    duration = "25 分钟"
    weight = 29
    image = "/img/mansion.jpg"
    tip = "在巨大的粉色糖果棒和棉花糖弹床之间，以连续蹲跳的惯性在弹床中心起跳，可直接冲上姜饼屋顶。"
  },
  @{
    file = "steampunk-party.md"
    title = "⚙️ 第二十九关：蒸汽朋克派对 (Steampunk Party)"
    desc = "人类一败涂地蒸汽朋克派对关卡攻略"
    difficulty = "⭐⭐⭐⭐☆"
    duration = "35 分钟"
    weight = 30
    image = "/img/swinging.jpg"
    tip = "踩在不断旋转的巨大活塞气缸顶，在活塞冲到最高端的瞬间反向起跳，可直接攀上蒸汽飞艇吊篮。"
  },
  @{
    file = "viking.md"
    title = "🪓 第三十关：维京 (Viking)"
    desc = "人类一败涂地维京关卡攻略"
    difficulty = "⭐⭐⭐⭐☆"
    duration = "35 分钟"
    weight = 31
    image = "/img/multiplayer.jpg"
    tip = "推动攻城槌到最大速度并抓住攻城槌，当攻城槌撞击城堡大门的瞬间松手，能将自己直接飞砸进城堡前院。"
  }
)

foreach ($level in $levels) {
  $file_path = "content/guides/" + $level.file
  Write-Host "Creating stub for" $level.title "at" $file_path
  
  $content = @"
---
title: "$($level.title)"
description: "$($level.desc)"
date: 2026-07-04
tags: [攻略, 关卡, 未完待续]
weight: $($level.weight)
---

# $($level.title)

> **当前状态**：📡 梦境信号传输中... 未完待续，敬请期待最新详细关卡攻略。
> **关卡参数**：难度指数 $($level.difficulty) | 预计时长 $($level.duration)

---

<div class="game-image-container">
  <img src="$($level.image)" alt="$($level.title) 关卡概览">
  <div class="img-caption">📸 $($level.title) 关卡实机演练 - 梦境参数同步中</div>
</div>

---

## 🔑 本关独家通关秘籍 (MISSION TIPS)

每个关卡都有其精妙的重力判定后门。虽然详细流程尚在录制中，但本站在此独家先行为您解锁该关卡的**通关秘籍**：

<div class="unlock-tip-box" style="background:rgba(0, 245, 255, 0.05) !important; border-color:var(--game-primary) !important; box-shadow:0 0 15px rgba(0, 245, 255, 0.15) !important;">
  <strong style="color:var(--game-primary);">⚡ 通关秘籍 ⚡</strong><br>
  $($level.tip)
</div>

---

*攻略编辑中... 最新数据源由 Bob 的脑电波持续补充中。如果您有更快的通关打法，欢迎联系我们投稿！*
"@

  $content | Out-File -FilePath $file_path -Encoding utf8
}

Write-Host "All stubs created successfully!"
