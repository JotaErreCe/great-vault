---
title: "OpenClaw"
source: "https://docs.openclaw.ai/"
author:
published:
created: 2026-05-04
description:
tags:
  - "clippings"
---
## OpenClaw 🦞

> *“EXFOLIATE! EXFOLIATE!”* — A space lobster, probably

**Any OS gateway for AI agents across Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, and more.**  
Send a message, get an agent response from your pocket. Run one Gateway across built-in channels, bundled channel plugins, WebChat, and mobile nodes.

## [Get Started](https://docs.openclaw.ai/start/getting-started)

Install OpenClaw and bring up the Gateway in minutes.

## [Run Onboarding](https://docs.openclaw.ai/start/wizard)

Guided setup with `openclaw onboard` and pairing flows.

## [Open the Control UI](https://docs.openclaw.ai/web/control-ui)

Launch the browser dashboard for chat, config, and sessions.

## What is OpenClaw?

OpenClaw is a **self-hosted gateway** that connects your favorite chat apps and channel surfaces — built-in channels plus bundled or external channel plugins such as Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, and more — to AI coding agents like Pi. You run a single Gateway process on your own machine (or a server), and it becomes the bridge between your messaging apps and an always-available AI assistant.

**Who is it for?** Developers and power users who want a personal AI assistant they can message from anywhere — without giving up control of their data or relying on a hosted service.

**What makes it different?**

- **Self-hosted**: runs on your hardware, your rules
- **Multi-channel**: one Gateway serves built-in channels plus bundled or external channel plugins simultaneously
- **Agent-native**: built for coding agents with tool use, sessions, memory, and multi-agent routing
- **Open source**: MIT licensed, community-driven

**What do you need?** Node 24 (recommended), or Node 22 LTS (`22.14+`) for compatibility, an API key from your chosen provider, and 5 minutes. For best quality and security, use the strongest latest-generation model available.

## How it works

<svg id="mermaid-_r_1j_-1777958713802" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="max-width: 753.09375px;" viewBox="0 0 753.09375 510" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-_r_1j_-1777958713802{font-family:inherit;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-_r_1j_-1777958713802.edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-_r_1j_-1777958713802.edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-_r_1j_-1777958713802.error-icon{fill:#a44141;}#mermaid-_r_1j_-1777958713802.error-text{fill:#ddd;stroke:#ddd;}#mermaid-_r_1j_-1777958713802.edge-thickness-normal{stroke-width:1px;}#mermaid-_r_1j_-1777958713802.edge-thickness-thick{stroke-width:3.5px;}#mermaid-_r_1j_-1777958713802.edge-pattern-solid{stroke-dasharray:0;}#mermaid-_r_1j_-1777958713802.edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-_r_1j_-1777958713802.edge-pattern-dashed{stroke-dasharray:3;}#mermaid-_r_1j_-1777958713802.edge-pattern-dotted{stroke-dasharray:2;}#mermaid-_r_1j_-1777958713802.marker{fill:lightgrey;stroke:lightgrey;}#mermaid-_r_1j_-1777958713802.marker.cross{stroke:lightgrey;}#mermaid-_r_1j_-1777958713802 svg{font-family:inherit;font-size:16px;}#mermaid-_r_1j_-1777958713802 p{margin:0;}#mermaid-_r_1j_-1777958713802.label{font-family:inherit;color:#ccc;}#mermaid-_r_1j_-1777958713802.cluster-label text{fill:#F9FFFE;}#mermaid-_r_1j_-1777958713802.cluster-label span{color:#F9FFFE;}#mermaid-_r_1j_-1777958713802.cluster-label span p{background-color:transparent;}#mermaid-_r_1j_-1777958713802.label text,#mermaid-_r_1j_-1777958713802 span{fill:#ccc;color:#ccc;}#mermaid-_r_1j_-1777958713802.node rect,#mermaid-_r_1j_-1777958713802.node circle,#mermaid-_r_1j_-1777958713802.node ellipse,#mermaid-_r_1j_-1777958713802.node polygon,#mermaid-_r_1j_-1777958713802.node path{fill:#1f2020;stroke:#ccc;stroke-width:1px;}#mermaid-_r_1j_-1777958713802.rough-node.label text,#mermaid-_r_1j_-1777958713802.node.label text,#mermaid-_r_1j_-1777958713802.image-shape.label,#mermaid-_r_1j_-1777958713802.icon-shape.label{text-anchor:middle;}#mermaid-_r_1j_-1777958713802.node.katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-_r_1j_-1777958713802.rough-node.label,#mermaid-_r_1j_-1777958713802.node.label,#mermaid-_r_1j_-1777958713802.image-shape.label,#mermaid-_r_1j_-1777958713802.icon-shape.label{text-align:center;}#mermaid-_r_1j_-1777958713802.node.clickable{cursor:pointer;}#mermaid-_r_1j_-1777958713802.root.anchor path{fill:lightgrey!important;stroke-width:0;stroke:lightgrey;}#mermaid-_r_1j_-1777958713802.arrowheadPath{fill:lightgrey;}#mermaid-_r_1j_-1777958713802.edgePath.path{stroke:lightgrey;stroke-width:1px;}#mermaid-_r_1j_-1777958713802.flowchart-link{stroke:lightgrey;fill:none;}#mermaid-_r_1j_-1777958713802.edgeLabel{background-color:hsl(0, 0%, 34.4117647059%);text-align:center;}#mermaid-_r_1j_-1777958713802.edgeLabel p{background-color:hsl(0, 0%, 34.4117647059%);}#mermaid-_r_1j_-1777958713802.edgeLabel rect{opacity:0.5;background-color:hsl(0, 0%, 34.4117647059%);fill:hsl(0, 0%, 34.4117647059%);}#mermaid-_r_1j_-1777958713802.labelBkg{background-color:rgba(87.75, 87.75, 87.75, 0.5);}#mermaid-_r_1j_-1777958713802.cluster rect{fill:hsl(180, 1.5873015873%, 28.3529411765%);stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-_r_1j_-1777958713802.cluster text{fill:#F9FFFE;}#mermaid-_r_1j_-1777958713802.cluster span{color:#F9FFFE;}#mermaid-_r_1j_-1777958713802 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:inherit;font-size:12px;background:hsl(20, 1.5873015873%, 12.3529411765%);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-_r_1j_-1777958713802.flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-_r_1j_-1777958713802 rect.text{fill:none;stroke-width:0;}#mermaid-_r_1j_-1777958713802.icon-shape,#mermaid-_r_1j_-1777958713802.image-shape{background-color:hsl(0, 0%, 34.4117647059%);text-align:center;}#mermaid-_r_1j_-1777958713802.icon-shape p,#mermaid-_r_1j_-1777958713802.image-shape p{background-color:hsl(0, 0%, 34.4117647059%);padding:2px;}#mermaid-_r_1j_-1777958713802.icon-shape.label rect,#mermaid-_r_1j_-1777958713802.image-shape.label rect{opacity:0.5;background-color:hsl(0, 0%, 34.4117647059%);fill:hsl(0, 0%, 34.4117647059%);}#mermaid-_r_1j_-1777958713802.label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-_r_1j_-1777958713802.node.label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-_r_1j_-1777958713802.node.neo-node{stroke:#ccc;}#mermaid-_r_1j_-1777958713802 [data-look="neo"].node rect,#mermaid-_r_1j_-1777958713802 [data-look="neo"].cluster rect,#mermaid-_r_1j_-1777958713802 [data-look="neo"].node polygon{stroke:url(#mermaid-_r_1j_-1777958713802-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-_r_1j_-1777958713802 [data-look="neo"].node path{stroke:url(#mermaid-_r_1j_-1777958713802-gradient);stroke-width:1px;}#mermaid-_r_1j_-1777958713802 [data-look="neo"].node.outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-_r_1j_-1777958713802 [data-look="neo"].node.neo-line path{stroke:#ccc;filter:none;}#mermaid-_r_1j_-1777958713802 [data-look="neo"].node circle{stroke:url(#mermaid-_r_1j_-1777958713802-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-_r_1j_-1777958713802 [data-look="neo"].node circle.state-start{fill:#000000;}#mermaid-_r_1j_-1777958713802 [data-look="neo"].icon-shape.icon{fill:url(#mermaid-_r_1j_-1777958713802-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-_r_1j_-1777958713802 [data-look="neo"].icon-shape.icon-neo path{stroke:url(#mermaid-_r_1j_-1777958713802-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-_r_1j_-1777958713802:root{--mermaid-font-family:inherit;}</style><g><marker id="mermaid-_r_1j_-1777958713802_flowchart-v2-pointEnd" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-_r_1j_-1777958713802_flowchart-v2-pointStart" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-_r_1j_-1777958713802_flowchart-v2-pointEnd-margin" viewBox="0 0 11.5 14" refX="11.5" refY="7" markerUnits="userSpaceOnUse" markerWidth="10.5" markerHeight="14" orient="auto"><path d="M 0 0 L 11.5 7 L 0 14 z" style="stroke-width: 0; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-_r_1j_-1777958713802_flowchart-v2-pointStart-margin" viewBox="0 0 11.5 14" refX="1" refY="7" markerUnits="userSpaceOnUse" markerWidth="11.5" markerHeight="14" orient="auto"><polygon points="0,7 11.5,14 11.5,0" style="stroke-width: 0; stroke-dasharray: 1, 0;"></polygon></marker><marker id="mermaid-_r_1j_-1777958713802_flowchart-v2-circleEnd" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" style="stroke-width: 1; stroke-dasharray: 1, 0;"></circle></marker><marker id="mermaid-_r_1j_-1777958713802_flowchart-v2-circleStart" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" style="stroke-width: 1; stroke-dasharray: 1, 0;"></circle></marker><marker id="mermaid-_r_1j_-1777958713802_flowchart-v2-circleEnd-margin" viewBox="0 0 10 10" refY="5" refX="12.25" markerUnits="userSpaceOnUse" markerWidth="14" markerHeight="14" orient="auto"><circle cx="5" cy="5" r="5" style="stroke-width: 0; stroke-dasharray: 1, 0;"></circle></marker><marker id="mermaid-_r_1j_-1777958713802_flowchart-v2-circleStart-margin" viewBox="0 0 10 10" refX="-2" refY="5" markerUnits="userSpaceOnUse" markerWidth="14" markerHeight="14" orient="auto"><circle cx="5" cy="5" r="5" style="stroke-width: 0; stroke-dasharray: 1, 0;"></circle></marker><marker id="mermaid-_r_1j_-1777958713802_flowchart-v2-crossEnd" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" style="stroke-width: 2; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-_r_1j_-1777958713802_flowchart-v2-crossStart" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" style="stroke-width: 2; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-_r_1j_-1777958713802_flowchart-v2-crossEnd-margin" viewBox="0 0 15 15" refX="17.7" refY="7.5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto"><path d="M 1,1 L 14,14 M 1,14 L 14,1" style="stroke-width: 2.5;"></path></marker><marker id="mermaid-_r_1j_-1777958713802_flowchart-v2-crossStart-margin" viewBox="0 0 15 15" refX="-3.5" refY="7.5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto"><path d="M 1,1 L 14,14 M 1,14 L 14,1" style="stroke-width: 2.5; stroke-dasharray: 1, 0;"></path></marker><g><g></g><g><path d="M255.875,243L260.042,243C264.208,243,272.542,243,280.208,243C287.875,243,294.875,243,298.375,243L301.875,243" id="mermaid-_r_1j_-1777958713802-L_A_B_0" style=";" data-edge="true" data-et="edge" data-id="L_A_B_0" data-points="W3sieCI6MjU1Ljg3NSwieSI6MjQzfSx7IngiOjI4MC44NzUsInkiOjI0M30seyJ4IjozMDUuODc1LCJ5IjoyNDN9XQ==" data-look="classic" marker-end="url(#mermaid-_r_1j_-1777958713802_flowchart-v2-pointEnd)"></path><path d="M382.116,216L395.113,185.833C408.109,155.667,434.101,95.333,460.672,65.167C487.242,35,514.391,35,527.965,35L541.539,35" id="mermaid-_r_1j_-1777958713802-L_B_C_0" style=";" data-edge="true" data-et="edge" data-id="L_B_C_0" data-points="W3sieCI6MzgyLjExNjM2MTE3Nzg4NDY0LCJ5IjoyMTZ9LHsieCI6NDYwLjA5Mzc1LCJ5IjozNX0seyJ4Ijo1NDUuNTM5MDYyNSwieSI6MzV9XQ==" data-look="classic" marker-end="url(#mermaid-_r_1j_-1777958713802_flowchart-v2-pointEnd)"></path><path d="M393.748,216L404.806,203.167C415.863,190.333,437.979,164.667,466.73,151.833C495.482,139,530.87,139,548.564,139L566.258,139" id="mermaid-_r_1j_-1777958713802-L_B_D_0" style=";" data-edge="true" data-et="edge" data-id="L_B_D_0" data-points="W3sieCI6MzkzLjc0ODM0NzM1NTc2OTIsInkiOjIxNn0seyJ4Ijo0NjAuMDkzNzUsInkiOjEzOX0seyJ4Ijo1NzAuMjU3ODEyNSwieSI6MTM5fV0=" data-look="classic" marker-end="url(#mermaid-_r_1j_-1777958713802_flowchart-v2-pointEnd)"></path><path d="M435.094,243L439.26,243C443.427,243,451.76,243,464.557,243C477.354,243,494.615,243,503.245,243L511.875,243" id="mermaid-_r_1j_-1777958713802-L_B_E_0" style=";" data-edge="true" data-et="edge" data-id="L_B_E_0" data-points="W3sieCI6NDM1LjA5Mzc1LCJ5IjoyNDN9LHsieCI6NDYwLjA5Mzc1LCJ5IjoyNDN9LHsieCI6NTE1Ljg3NSwieSI6MjQzfV0=" data-look="classic" marker-end="url(#mermaid-_r_1j_-1777958713802_flowchart-v2-pointEnd)"></path><path d="M393.748,270L404.806,282.833C415.863,295.667,437.979,321.333,461.786,334.167C485.594,347,511.094,347,523.844,347L536.594,347" id="mermaid-_r_1j_-1777958713802-L_B_F_0" style=";" data-edge="true" data-et="edge" data-id="L_B_F_0" data-points="W3sieCI6MzkzLjc0ODM0NzM1NTc2OTIsInkiOjI3MH0seyJ4Ijo0NjAuMDkzNzUsInkiOjM0N30seyJ4Ijo1NDAuNTkzNzUsInkiOjM0N31d" data-look="classic" marker-end="url(#mermaid-_r_1j_-1777958713802_flowchart-v2-pointEnd)"></path><path d="M381.482,270L394.584,302.167C407.686,334.333,433.89,398.667,450.492,430.833C467.094,463,474.094,463,477.594,463L481.094,463" id="mermaid-_r_1j_-1777958713802-L_B_G_0" style=";" data-edge="true" data-et="edge" data-id="L_B_G_0" data-points="W3sieCI6MzgxLjQ4MTg4OTIwNDU0NTQ0LCJ5IjoyNzB9LHsieCI6NDYwLjA5Mzc1LCJ5Ijo0NjN9LHsieCI6NDg1LjA5Mzc1LCJ5Ijo0NjN9XQ==" data-look="classic" marker-end="url(#mermaid-_r_1j_-1777958713802_flowchart-v2-pointEnd)"></path></g><g><g><g data-id="L_A_B_0" transform="translate(0, 0)"></g></g><g><g data-id="L_B_C_0" transform="translate(0, 0)"></g></g><g><g data-id="L_B_D_0" transform="translate(0, 0)"></g></g><g><g data-id="L_B_E_0" transform="translate(0, 0)"></g></g><g><g data-id="L_B_F_0" transform="translate(0, 0)"></g></g><g><g data-id="L_B_G_0" transform="translate(0, 0)"></g></g></g><g><g id="mermaid-_r_1j_-1777958713802-flowchart-A-0" data-look="classic" transform="translate(131.9375, 243)"><rect style="" x="-123.9375" y="-27" width="247.875" height="54"></rect><g style="" transform="translate(-93.9375, -12)"><rect></rect><foreignObject width="187.875" height="24"><p>Chat apps + plugins</p></foreignObject></g></g><g id="mermaid-_r_1j_-1777958713802-flowchart-B-1" data-look="classic" transform="translate(370.484375, 243)"><rect style="" x="-64.609375" y="-27" width="129.21875" height="54"></rect><g style="" transform="translate(-34.609375, -12)"><rect></rect><foreignObject width="69.21875" height="24"><p>Gateway</p></foreignObject></g></g><g id="mermaid-_r_1j_-1777958713802-flowchart-C-3" data-look="classic" transform="translate(615.09375, 35)"><rect style="" x="-69.5546875" y="-27" width="139.109375" height="54"></rect><g style="" transform="translate(-39.5546875, -12)"><rect></rect><foreignObject width="79.109375" height="24"><p>Pi agent</p></foreignObject></g></g><g id="mermaid-_r_1j_-1777958713802-flowchart-D-5" data-look="classic" transform="translate(615.09375, 139)"><rect style="" x="-44.8359375" y="-27" width="89.671875" height="54"></rect><g style="" transform="translate(-14.8359375, -12)"><rect></rect><foreignObject width="29.671875" height="24"><p>CLI</p></foreignObject></g></g><g id="mermaid-_r_1j_-1777958713802-flowchart-E-7" data-look="classic" transform="translate(615.09375, 243)"><rect style="" x="-99.21875" y="-27" width="198.4375" height="54"></rect><g style="" transform="translate(-69.21875, -12)"><rect></rect><foreignObject width="138.4375" height="24"><p>Web Control UI</p></foreignObject></g></g><g id="mermaid-_r_1j_-1777958713802-flowchart-F-9" data-look="classic" transform="translate(615.09375, 347)"><rect style="" x="-74.5" y="-27" width="149" height="54"></rect><g style="" transform="translate(-44.5, -12)"><rect></rect><foreignObject width="89" height="24"><p>macOS app</p></foreignObject></g></g><g id="mermaid-_r_1j_-1777958713802-flowchart-G-11" data-look="classic" transform="translate(615.09375, 463)"><rect style="" x="-130" y="-39" width="260" height="78"></rect><g style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><p>iOS and Android nodes</p></foreignObject></g></g></g></g></g><defs></defs><defs></defs><linearGradient id="mermaid-_r_1j_-1777958713802-gradient" gradientUnits="objectBoundingBox" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#cccccc" stop-opacity="1"></stop><stop offset="100%" stop-color="hsl(180, 0%, 18.3529411765%)" stop-opacity="1"></stop></linearGradient></svg>

The Gateway is the single source of truth for sessions, routing, and channel connections.

## Key capabilities

## [Multi-channel gateway](https://docs.openclaw.ai/channels)

Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat, and more with a single Gateway process.

## [Plugin channels](https://docs.openclaw.ai/tools/plugin)

Bundled plugins add Matrix, Nostr, Twitch, Zalo, and more in normal current releases.

## [Multi-agent routing](https://docs.openclaw.ai/concepts/multi-agent)

Isolated sessions per agent, workspace, or sender.

## [Media support](https://docs.openclaw.ai/nodes/images)

Send and receive images, audio, and documents.

## [Web Control UI](https://docs.openclaw.ai/web/control-ui)

Browser dashboard for chat, config, sessions, and nodes.

## [Mobile nodes](https://docs.openclaw.ai/nodes)

Pair iOS and Android nodes for Canvas, camera, and voice-enabled workflows.

## Quick start

Need the full install and dev setup? See [Getting Started](https://docs.openclaw.ai/start/getting-started).

## Dashboard

Open the browser Control UI after the Gateway starts.

- Local default: [http://127.0.0.1:18789/](http://127.0.0.1:18789/)
- Remote access: [Web surfaces](https://docs.openclaw.ai/web) and [Tailscale](https://docs.openclaw.ai/gateway/tailscale)

![OpenClaw](https://mintcdn.com/clawdhub/FaXdIfo7gPK_jSWb/whatsapp-openclaw.jpg?w=2500&fit=max&auto=format&n=FaXdIfo7gPK_jSWb&q=85&s=7050f3dda374e9a1adedf3cd08357338)

## Configuration (optional)

Config lives at `~/.openclaw/openclaw.json`.

- If you **do nothing**, OpenClaw uses the bundled Pi binary in RPC mode with per-sender sessions.
- If you want to lock it down, start with `channels.whatsapp.allowFrom` and (for groups) mention rules.

Example:

```json5
{
  channels: {
    whatsapp: {
      allowFrom: ["+15555550123"],
      groups: { "*": { requireMention: true } },
    },
  },
  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },
}
```

## Start here

## [Docs hubs](https://docs.openclaw.ai/start/hubs)

All docs and guides, organized by use case.

## [Configuration](https://docs.openclaw.ai/gateway/configuration)

Core Gateway settings, tokens, and provider config.

## [Remote access](https://docs.openclaw.ai/gateway/remote)

SSH and tailnet access patterns.

## [Channels](https://docs.openclaw.ai/channels/telegram)

Channel-specific setup for Feishu, Microsoft Teams, WhatsApp, Telegram, Discord, and more.

## [Nodes](https://docs.openclaw.ai/nodes)

iOS and Android nodes with pairing, Canvas, camera, and device actions.

## [Help](https://docs.openclaw.ai/help)

Common fixes and troubleshooting entry point.

## Learn more

## [Full feature list](https://docs.openclaw.ai/concepts/features)

Complete channel, routing, and media capabilities.

## [Multi-agent routing](https://docs.openclaw.ai/concepts/multi-agent)

Workspace isolation and per-agent sessions.

## [Security](https://docs.openclaw.ai/gateway/security)

Tokens, allowlists, and safety controls.

## [Troubleshooting](https://docs.openclaw.ai/gateway/troubleshooting)

Gateway diagnostics and common errors.

## [About and credits](https://docs.openclaw.ai/reference/credits)

Project origins, contributors, and license.