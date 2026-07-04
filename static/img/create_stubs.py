# -*- coding: utf-8 -*-
import os

levels = [
    {
        "file": "mansion.md",
        "title": "🏰 Level 1: Mansion",
        "desc": "Human: Fall Flat Mansion full walkthrough - Basic tutorial guide",
        "difficulty": "⭐☆☆☆☆",
        "duration": "8 Mins",
        "weight": 1,
        "image": "/img/mansion.jpg",
        "tip": "Jump and grab the crane hook at the high platform, swing to the furthest and highest point, release hook and press jump to fly directly to the landing helicopter platform.",
        "is_stub": False
    },
    {
        "file": "factory.md",
        "title": "🏭 Level 2: Factory",
        "desc": "Human: Fall Flat Factory full walkthrough - Conveyor belts and heavy piston puzzles",
        "difficulty": "⭐⭐☆☆☆",
        "duration": "15 Mins",
        "weight": 2,
        "image": "/img/factory.jpg",
        "tip": "Use the crane arm at the big pit as a horizontal bar, release hook and press jump at the maximum elevation angle to trigger a long-distance slingshot glide.",
        "is_stub": False
    },
    {
        "file": "train.md",
        "title": "🚂 Level 3: Train",
        "desc": "Human: Fall Flat Train level guide & secrets",
        "difficulty": "⭐⭐☆☆☆",
        "duration": "12 Mins",
        "weight": 3,
        "image": "/img/climbing.jpg",
        "tip": "Use the gaps and edges on top of the train compartments to climb, allowing you to bypass the barrier gates directly and skip the switch-pulling puzzle steps.",
        "is_stub": True
    },
    {
        "file": "carry.md",
        "title": "📦 Level 4: Carry",
        "desc": "Human: Fall Flat Carry level guide & secrets",
        "difficulty": "⭐⭐☆☆☆",
        "duration": "10 Mins",
        "weight": 4,
        "image": "/img/factory.jpg",
        "tip": "Use both hands to push/pull the large box backwards as a shield, then grab the highest edge when jumping to leap over most high railings directly.",
        "is_stub": True
    },
    {
        "file": "mountain.md",
        "title": "⛰️ Level 5: Mountain",
        "desc": "Human: Fall Flat Mountain level guide & secrets",
        "difficulty": "⭐⭐⭐☆☆",
        "duration": "20 Mins",
        "weight": 5,
        "image": "/img/climbing.jpg",
        "tip": "Face the mountain wall and grab it with both hands, then swing your head left and right rhythmically to trigger the single-hand high-reach grab, allowing you to climb over steep cliffs directly.",
        "is_stub": True
    },
    {
        "file": "demolition.md",
        "title": "🏗️ Level 6: Demolition",
        "desc": "Human: Fall Flat Demolition level guide & secrets",
        "difficulty": "⭐⭐⭐☆☆",
        "duration": "18 Mins",
        "weight": 6,
        "image": "/img/swinging.jpg",
        "tip": "Grab the wrecking ball and swing it hard toward the glass window, which can drastically reduce the number of hits needed to shatter it, or jump directly onto the abandoned steel frame to climb over the wall.",
        "is_stub": True
    },
    {
        "file": "castle.md",
        "title": "🏰 Level 7: Castle",
        "desc": "Human: Fall Flat Castle level guide & secrets",
        "difficulty": "⭐⭐⭐☆☆",
        "duration": "25 Mins",
        "weight": 7,
        "image": "/img/climbing.jpg",
        "tip": "When using the catapult, put yourself into the catapult spoon, pull down the lever, and launch yourself directly into the deepest part of the castle using gravity.",
        "is_stub": True
    },
    {
        "file": "water.md",
        "title": "⛵ Level 8: Water",
        "desc": "Human: Fall Flat Water level guide & secrets",
        "difficulty": "⭐⭐⭐☆☆",
        "duration": "25 Mins",
        "weight": 8,
        "image": "/img/multiplayer.jpg",
        "tip": "When steering the speedboat, release the controls and move in the opposite direction to execute a drift turn. A propeller boost jump underwater can launch you over the high slope.",
        "is_stub": True
    },
    {
        "file": "power.md",
        "title": "⚡ Level 9: Power",
        "desc": "Human: Fall Flat Power level guide & secrets",
        "difficulty": "⭐⭐⭐☆☆",
        "duration": "30 Mins",
        "weight": 9,
        "image": "/img/factory.jpg",
        "tip": "Connect the battery cables to the matching terminals of the backup circuit board to trigger a short circuit, or grab the generator fan blades to swing directly to the balcony on the opposite side.",
        "is_stub": True
    },
    {
        "file": "aztec.md",
        "title": "🗿 Level 10: Aztec",
        "desc": "Human: Fall Flat Aztec level guide & secrets",
        "difficulty": "⭐⭐⭐⭐☆",
        "duration": "30 Mins",
        "weight": 10,
        "image": "/img/mansion.jpg",
        "tip": "When the large boulder rolls down, jump and grab it in the opposite direction of its roll. Use its tangential velocity to fling yourself directly onto the bridge at the exit.",
        "is_stub": True
    },
    {
        "file": "dark.md",
        "title": "🌃 Level 11: Dark",
        "desc": "Human: Fall Flat Dark level guide & secrets",
        "difficulty": "⭐⭐⭐⭐☆",
        "duration": "30 Mins",
        "weight": 11,
        "image": "/img/cover.jpg",
        "tip": "After plugging the red and blue wires into the distribution box, pull out the backup generator plug and hang it on the pulley wire to zipline directly to the backyard exit.",
        "is_stub": True
    },
    {
        "file": "steam.md",
        "title": "💨 Level 12: Steam",
        "desc": "Human: Fall Flat Steam level guide & secrets",
        "difficulty": "⭐⭐⭐☆☆",
        "duration": "30 Mins",
        "weight": 12,
        "image": "/img/swinging.jpg",
        "tip": "Step on the high-pressure steam vent, and jump the moment the vent releases a steam burst. The steam will lift you up, launching you instantly into the high pipe tunnel.",
        "is_stub": True
    },
    {
        "file": "ice.md",
        "title": "❄️ Level 13: Ice",
        "desc": "Human: Fall Flat Ice level guide & secrets",
        "difficulty": "⭐⭐⭐☆☆",
        "duration": "25 Mins",
        "weight": 13,
        "image": "/img/cover.jpg",
        "tip": "Place a wooden plank on the ice slope and slide down using your body as a drag brake to gain double the jump velocity before reaching the cliff edge.",
        "is_stub": True
    },
    {
        "file": "thermal.md",
        "title": "🌋 Level 14: Thermal",
        "desc": "Human: Fall Flat Thermal level guide & secrets",
        "difficulty": "⭐⭐⭐⭐☆",
        "duration": "35 Mins",
        "weight": 14,
        "image": "/img/swinging.jpg",
        "tip": "Grab the bottom bar of the hot air balloon. When it reaches its peak height, swing your body sideways and let go to float down directly into the exit cave.",
        "is_stub": True
    },
    {
        "file": "golf.md",
        "title": "⛳ Level 15: Golf",
        "desc": "Human: Fall Flat Golf level guide & secrets",
        "difficulty": "⭐⭐⭐☆☆",
        "duration": "25 Mins",
        "weight": 15,
        "image": "/img/multiplayer.jpg",
        "tip": "When hitting the golf ball, hang Bob directly on the club and act as a gravity pendulum to strike the ball with massive force, putting it into the far hole in a single shot.",
        "is_stub": True
    },
    {
        "file": "city.md",
        "title": "🏙️ Level 16: City",
        "desc": "Human: Fall Flat City level guide & secrets",
        "difficulty": "⭐⭐⭐⭐☆",
        "duration": "30 Mins",
        "weight": 16,
        "image": "/img/hero_banner.jpg",
        "tip": "Utilize the continuous bouncing force of the trampoline, and jump on the third bounce (when the amplitude is largest) to jump directly onto the rooftop helipad.",
        "is_stub": True
    },
    {
        "file": "forest.md",
        "title": "🌲 Level 17: Forest",
        "desc": "Human: Fall Flat Forest level guide & secrets",
        "difficulty": "⭐⭐⭐⭐☆",
        "duration": "35 Mins",
        "weight": 17,
        "image": "/img/climbing.jpg",
        "tip": "Fell the trees to make them fall between cliffs to create a bridge, or use the rope to hook onto tree trunks to execute pendulum swings across the deep chasms.",
        "is_stub": True
    },
    {
        "file": "laboratory.md",
        "title": "🔬 Level 18: Laboratory",
        "desc": "Human: Fall Flat Laboratory level guide & secrets",
        "difficulty": "⭐⭐⭐⭐☆",
        "duration": "30 Mins",
        "weight": 18,
        "image": "/img/factory.jpg",
        "tip": "Use the electromagnet to attract the steel sphere as a suspended basket, and jump the moment it powers on to use the electromagnetic repulsion to fling yourself into the high pipes.",
        "is_stub": True
    },
    {
        "file": "lumber.md",
        "title": "🪵 Level 19: Lumber",
        "desc": "Human: Fall Flat Lumber level guide & secrets",
        "difficulty": "⭐⭐⭐⭐☆",
        "duration": "35 Mins",
        "weight": 19,
        "image": "/img/factory.jpg",
        "tip": "Bind multiple logs together to make a raft, steer the paddle to stay balanced in the center, and you can float directly through the violent rapids.",
        "is_stub": True
    },
    {
        "file": "red-rock.md",
        "title": "🏜️ Level 20: Red Rock",
        "desc": "Human: Fall Flat Red Rock level guide & secrets",
        "difficulty": "⭐⭐⭐⭐☆",
        "duration": "30 Mins",
        "weight": 20,
        "image": "/img/mansion.jpg",
        "tip": "Use the airflow generated by the fans combined with the glider to perform long-distance glides, flying directly over the vast canyon terrain.",
        "is_stub": True
    },
    {
        "file": "tower.md",
        "title": "🗼 Level 21: Tower",
        "desc": "Human: Fall Flat Tower level guide & secrets",
        "difficulty": "⭐⭐⭐⭐☆",
        "duration": "35 Mins",
        "weight": 21,
        "image": "/img/climbing.jpg",
        "tip": "When climbing the rotating gear on the tower wall, jump in the direction of the gear's rotation to let the tangential force fling you to the opposite water pipe.",
        "is_stub": True
    },
    {
        "file": "miniature.md",
        "title": "🔍 Level 22: Miniature",
        "desc": "Human: Fall Flat Miniature level guide & secrets",
        "difficulty": "⭐⭐⭐☆☆",
        "duration": "25 Mins",
        "weight": 22,
        "image": "/img/hero_banner.jpg",
        "tip": "Between the giant microwave and the toy car, step on the trunk of the toy car and jump to use the car's collision box to bounce directly onto the table.",
        "is_stub": True
    },
    {
        "file": "copper-world.md",
        "title": "🪙 Level 23: Copper World",
        "desc": "Human: Fall Flat Copper World level guide & secrets",
        "difficulty": "⭐⭐⭐⭐☆",
        "duration": "35 Mins",
        "weight": 23,
        "image": "/img/factory.jpg",
        "tip": "Operate the giant electromagnetic crane to grab the battery directly in mid-air and drop it into the slot, saving you the effort of pulling power switches.",
        "is_stub": True
    },
    {
        "file": "port.md",
        "title": "⚓ Level 24: Port",
        "desc": "Human: Fall Flat Port level guide & secrets",
        "difficulty": "⭐⭐⭐⭐☆",
        "duration": "30 Mins",
        "weight": 24,
        "image": "/img/mansion.jpg",
        "tip": "Use the crane hook to pull the cargo ship closer to the dock, jump onto the ship's mast, and swing directly to the lighthouse on the opposite shore to skip container moving.",
        "is_stub": True
    },
    {
        "file": "underwater.md",
        "title": "🐳 Level 25: Underwater",
        "desc": "Human: Fall Flat Underwater level guide & secrets",
        "difficulty": "⭐⭐⭐⭐☆",
        "duration": "35 Mins",
        "weight": 25,
        "image": "/img/multiplayer.jpg",
        "tip": "When diving, grab the side wing of the underwater scooter and use the thruster's momentum to crash directly through the fragile glass panels at the bottom of the sea.",
        "is_stub": True
    },
    {
        "file": "hike.md",
        "title": "🥾 Level 26: Hike",
        "desc": "Human: Fall Flat Hike level guide & secrets",
        "difficulty": "⭐⭐⭐☆☆",
        "duration": "25 Mins",
        "weight": 26,
        "image": "/img/climbing.jpg",
        "tip": "Use a loose boulder as a seesaw, place a box on one end, and jump from a high place onto the other end to launch the box up onto the cliff.",
        "is_stub": True
    },
    {
        "file": "test-chamber.md",
        "title": "🧬 Level 27: Test Chamber",
        "desc": "Human: Fall Flat Test Chamber level guide & secrets",
        "difficulty": "⭐⭐⭐⭐☆",
        "duration": "30 Mins",
        "weight": 27,
        "image": "/img/factory.jpg",
        "tip": "Use the gravity inversion device. The moment gravity reverses, grab the edge of the ceiling with both hands to slide directly into the exit room.",
        "is_stub": True
    },
    {
        "file": "candyland.md",
        "title": "🍭 Level 28: Candyland",
        "desc": "Human: Fall Flat Candyland level guide & secrets",
        "difficulty": "⭐⭐⭐☆☆",
        "duration": "25 Mins",
        "weight": 28,
        "image": "/img/mansion.jpg",
        "tip": "Between the giant pink candy canes and the marshmallow trampoline, jump at the center of the trampoline with continuous crouching momentum to land directly on the gingerbread roof.",
        "is_stub": True
    },
    {
        "file": "steampunk-party.md",
        "title": "⚙️ Level 29: Steampunk Party",
        "desc": "Human: Fall Flat Steampunk Party level guide & secrets",
        "difficulty": "⭐⭐⭐⭐☆",
        "duration": "35 Mins",
        "weight": 29,
        "image": "/img/swinging.jpg",
        "tip": "Step on the top of the continuously moving giant piston cylinder, and jump in the opposite direction at its peak height to climb directly onto the steam airship basket.",
        "is_stub": True
    },
    {
        "file": "viking.md",
        "title": "🪓 Level 30: Viking",
        "desc": "Human: Fall Flat Viking level guide & secrets",
        "difficulty": "⭐⭐⭐⭐☆",
        "duration": "35 Mins",
        "weight": 30,
        "image": "/img/multiplayer.jpg",
        "tip": "Push the battering ram to its maximum speed and grab it. The moment it hits the castle gate, let go to fling yourself directly into the castle front yard.",
        "is_stub": True
    }
]

stub_template = """---
title: "{title}"
description: "{desc}"
date: 2026-07-04
tags: [Walkthrough, Level, ComingSoon]
weight: {weight}
---

# {title}

> **Current Status**: 📡 Dream signals syncing... To be continued, stay tuned for the latest detailed level guides.
> **Level Matrix**: Difficulty {difficulty} | Est. Duration {duration}

---

<div class="game-image-container">
  <img src="{image}" alt="{title} Level Overview">
  <div class="img-caption">📸 {title} Level Overview - Dreamscape Coordinate Calibration</div>
</div>

---

## 🔑 Level Clearance Secrets (MISSION TIPS)

Every dream level features unique gaps in its physics logic. While our full walkthrough captures are being uploaded, we have unlocked the **Clearance Secret** for you:

<div class="unlock-tip-box" style="background:rgba(0, 245, 255, 0.05) !important; border-color:var(--game-primary) !important; box-shadow:0 0 15px rgba(0, 245, 255, 0.15) !important;">
  <strong style="color:var(--game-primary);">⚡ Clearance Secret ⚡</strong><br>
  {tip}
</div>

---

*Guides editing... Wobbly Bob telemetry is feeded live from Bobs worldwide. Got a faster route? Submit your highlights to us!*
"""

os.makedirs("content/guides", exist_ok=True)

# Generate stubs
for lvl in levels:
    if lvl["is_stub"]:
        filepath = os.path.join("content/guides", lvl["file"])
        content = stub_template.format(**lvl)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

# Generate the main guides list (_index.md)
index_filepath = "content/guides/_index.md"
index_header = """---
title: "📖 Level Guides"
description: "Human: Fall Flat all level walkthroughs and secrets"
---

# 📖 Level Selection Panel (MISSIONS)

Welcome to the dreamscape missions console. We have cataloged difficulty levels, average completion times, and **Clearance Secrets** for all official maps. Select a card below to access specific data terminals:

---

## 🗺️ Official Dreams Catalogue

<div class="level-select-grid">"""

index_footer = """
</div>

---

<div class="unlock-tip-box" style="background:rgba(255,107,0,0.05) !important; border-color:var(--game-accent) !important; box-shadow:0 0 15px rgba(255,107,0,0.15) !important;">
  <strong style="color:var(--game-accent);">【Hidden Achievements warning】</strong><br>
  Every level features official achievements (e.g., scoring a goal in Mansion, or clearing Factory without using conveyor belts). When walking through, make sure to explore off-road corners to unlock these special achievements!
</div>
"""

cards_html = []
for lvl in levels:
    name_clean = lvl["file"].replace(".md", "")
    badge = '<span style="color:#00ff66; font-size:0.8rem;">● DONE</span>' if not lvl["is_stub"] else '<span style="color:#ffcc00; font-size:0.8rem;">● COMING</span>'
    btn_text = 'Open Walkthrough' if not lvl["is_stub"] else 'Get Secret Tip'
    
    card = f"""
  <!-- {lvl['title']} Card -->
  <div class="level-select-card">
    <img src="{lvl['image']}" alt="{lvl['title']}" class="level-select-img">
    <div class="level-select-body">
      <div class="level-select-title">
        {badge}
        {lvl['title']}
      </div>
      <p style="font-size:0.85rem; color:var(--game-text-muted); line-height:1.4; margin:0.5rem 0;">{lvl['desc']}</p>
      <a href="/guides/{name_clean}/" class="btn-cyber" style="padding:0.4rem 1rem; font-size:0.8rem; margin-top:1rem; align-self:flex-start;">{btn_text}</a>
      <div class="level-select-info">
        <span>Diff: {lvl['difficulty']}</span>
        <span>Est: {lvl['duration']}</span>
      </div>
    </div>
  </div>"""
    cards_html.append(card)

full_index_content = index_header + "".join(cards_html) + index_footer

with open(index_filepath, "w", encoding="utf-8") as f:
    f.write(full_index_content)

print("All stubs and guides index generated successfully!")
