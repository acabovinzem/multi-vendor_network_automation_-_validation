# Multi-Vendor Network Automation & Validation

A hands-on lab project demonstrating how to automate network devices
from different vendors using a single Python script. Built on Nornir,
Netmiko, and Containerlab.

## What This Project Demonstrates

The core idea is simple: instead of SSHing into each router and typing
commands manually, you define your devices in a YAML inventory and run
one script that handles all of them. The same script works across
vendors because the inventory tells Nornir which driver to use for
each device.

## Current Status

| Component | Status |
|---|---|
| Python + Nornir framework | ✅ Working |
| YAML inventory (hosts/groups/defaults) | ✅ Built |
| Containerlab lab in Kali VM | ✅ Running |
| FRRouting containers (r1, r2) | ✅ Deployed |
| SSH enabled on FRR containers | ⚠️ In progress |
| Second vendor (Arista cEOS) | ❌ Not started |
| Validation tasks | ❌ Not started |
| Jinja2 config templates | ❌ Not started |

## Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3.9 |
| Orchestration | Nornir 3.5 |
| SSH Connection | Netmiko 4.6 |
| Inventory Format | YAML |
| Lab Orchestrator | Containerlab |
| Container Runtime | Docker |
| Network OS (lab) | FRRouting 10.4.4 |
| Guest VM | Kali Linux (ARM64) |
| Host | MacBook Air M1 |
| Version Control | Git + GitHub |

## Lab Topology
┌─────────────┐ ┌─────────────┐
│ r1 │─────────│ r2 │
│ 172.20.20.2 │ eth1 │ 172.20.20.3 │
│ FRR │ │ FRR │
└─────────────┘ └─────────────┘

Both routers run FRRouting inside Docker containers, managed by
Containerlab. Management IPs are assigned automatically on the
172.20.20.0/24 network.

## Project Structure
.
├── README.md
├── requirements.txt
├── config.yaml # Nornir config (points to inventory)
├── test_multi_vendor.py # Main automation script
└── inventory/
├── hosts.yaml # Device list with IPs
├── groups.yaml # Vendor/platform mapping
└── defaults.yaml # Shared credentials