---
title: "How to Play Human: Fall Flat with Friends - Steam, Remote Play, Crossplay & 8-Player Co-op Guide"
description: "Complete 2026 multiplayer guide: Steam invites, Remote Play Together (friends play free), crossplay limits, Switch split-screen, 8-player public lobbies, and connection troubleshooting."
date: 2026-09-20
tags: [multiplayer, steam, remote-play, crossplay]
weight: 1
---

# How to Play Human: Fall Flat with Friends — Full Multiplayer Guide

Human: Fall Flat supports up to **8 players online**, and co-op turns the physics engine into pure chaos — coordinated carrying, mutual throwing, human ladders up walls. But getting friends in involves three separate systems: Steam invites, Remote Play Together, and crossplay limits. This guide covers the 2026 state of each.

## 1. Steam Online Co-op (up to 8 players)

If you and your friends all own the Steam version, this is the simplest path:

1. Enter any level, press `Shift + Tab` to open the Steam overlay, right-click the friend in your friends list, and choose **"Invite to game"**.
2. Your friend sees a popup on their end, accepts, and drops into your level.
3. Up to 8 players can share a session; beyond that, new invites are rejected.
4. Want strangers instead? Pick **"Public game"** on the main menu to open the public lobby browser and match into global rooms.

Always invite from the Steam friends list, not from inside the game — there is no in-game invite button, all invitations go through the Steam overlay.

## 2. Steam Remote Play Together: Friends Play Free

This is the most-asked feature. **Steam Remote Play Together** lets the host stream the game to friends, who then control their own Bob remotely using their own keyboard, mouse, or gamepad. Rules:

- Only the host needs to own Human: Fall Flat. Invited friends **do not need to purchase**.
- Once in-game, open the Steam overlay, right-click a friend, and pick "Remote Play Together invite".
- Friends see the host's stream but control their own character.
- Latency depends on the host's upload bandwidth and the geographic distance between players. Pick a host close to the rest of the group.
- Remote Play Together supports up to 4 remote friends. This is separate from the 8-player online cap, but in practice, four-plus remote players get noticeably laggy.

Note that Remote Play Together is "stream + remote input", not true peer-to-peer. Picture quality fluctuates with bandwidth, and poor networks will cause mosaic artifacts and input lag.

## 3. Crossplay: Which Platforms Can Play Together

This is where most people get stuck. The 2026 crossplay situation:

- **Xbox ↔ Windows PC (Microsoft Store version)**: works, because both use Xbox Live networking.
- **Steam ↔ Xbox**: **not supported**. Steam uses Steam networking and is isolated from Xbox pools.
- **PlayStation 4 ↔ PlayStation 5**: works, but both must run the PS4 version of the game.
- **Nintendo Switch**: same-family only. A Switch 2-exclusive edition is scheduled for summer 2026.
- **Mobile (Android ↔ iOS)**: crossplay works, but mobile cannot connect to PC or console.
- **Cross-save**: **not supported**. Progress earned on Steam does not carry over to Xbox or vice versa.

The takeaway: confirm platforms before buying. Steam is the safest pick (most Workshop content, largest community). If your friends are on Xbox, you must buy the Microsoft Store version, not Steam.

## 4. Nintendo Switch Local Split-Screen (2 Players)

The Switch version has a **local 2-player split-screen** mode: split a pair of Joy-Con or plug in a Pro controller, and one Switch console runs two players side by side. Note that split-screen cannot be combined with online play — you're either 2 players local, or up to 8 players online, never both.

## 5. Common Connection Problems and Fixes

**Friend doesn't see the invite.** You probably tried to invite from inside the game. Press Shift+Tab and right-click the friend in the Steam overlay friends list instead.

**Friend joins but hangs on loading.** Mismatched game versions. Steam auto-updates; on Epic or Microsoft Store you may need to manually check for updates.

**High latency, drifting inputs.** Host's upload bandwidth is low, or players are on different continents. Host should switch to wired ethernet, and Remote Play Together can lower stream quality. Try playing at hours when both sides' time zones overlap.

**Public lobby won't connect.** Strict NAT. Enable UPnP on the router, or turn on "Steam relay" in Steam settings.

**Crossplay friend not found.** Crossplay itself isn't supported between those platforms — see section 3 and confirm compatibility.

## 6. Co-op Play Tips

- **Two-person carrying**: long planks, batteries, and other large objects move faster when each of you grabs an end, and you can fit through narrow gaps.
- **Human ladder**: one player hugs the wall, the second climbs on their shoulders and pulls the first up — far easier than solo climbing.
- **Throw relays**: toss small items from a high ledge to a friend below rather than walking them down the stairs.
- **Grab caution**: grabbing cuts both ways. In a panic you'll grab a friend and drag them off the cliff with you — let go before ledges.

For movement mechanics see [Core Physics Tricks Guide](/gameplay/physics-tips/), and for full level solutions see the [30-Level Walkthrough Index](/guides/).

---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How many players can play Human: Fall Flat online together?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Steam online co-op supports up to 8 players simultaneously. Nintendo Switch local split-screen supports 2 players, but cannot be combined with online play."
      }
    },
    {
      "@type": "Question",
      "name": "Does Steam Remote Play Together require my friend to own the game?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Only the host needs to own Human: Fall Flat. Invited friends join via stream and control their own character without purchasing the game. Remote Play Together supports up to 4 remote friends."
      }
    },
    {
      "@type": "Question",
      "name": "Can Steam players crossplay with Xbox players in Human: Fall Flat?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. The Steam version uses Steam networking and is isolated from Xbox pools. Only the Microsoft Store PC version can crossplay with Xbox. If you want to play with Xbox friends, you must buy the Microsoft Store version, not Steam."
      }
    },
    {
      "@type": "Question",
      "name": "Does Human: Fall Flat support cross-save between platforms?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Cross-save is not supported. Progress, unlocks, and skins earned on Steam do not sync to Xbox, PlayStation, or Switch, and vice versa. Each platform keeps progress independently."
      }
    },
    {
      "@type": "Question",
      "name": "How do I invite a Steam friend to Human: Fall Flat?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Enter any level, press Shift+Tab to open the Steam overlay, right-click the friend in your friends list, and choose \"Invite to game\". Invitations must be sent from the Steam friends list — there is no in-game invite button."
      }
    },
    {
      "@type": "Question",
      "name": "How do I fix high latency in Human: Fall Flat multiplayer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Have the host switch to a wired ethernet connection and close bandwidth-heavy apps. For Remote Play Together, lower the stream quality in Steam settings. For cross-continent play, pick hours when both time zones overlap. If public lobbies won't connect, enable UPnP on your router or turn on Steam relay."
      }
    }
  ]
}
</script>
