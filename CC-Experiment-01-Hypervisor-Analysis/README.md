# Performance Analysis of Type-1 and Type-2 Hypervisors

---

## Executive Summary

This repository contains the experimental setup, benchmark results, performance visualizations, screenshots, and technical analysis for comparing a Type-1 Hypervisor (**Proxmox VE**) and a Type-2 Hypervisor (**VMware Workstation**).

Both environments were configured with comparable Ubuntu virtual machines using **2 vCPU, 2 GB RAM, and 20 GB virtual disk**. The same `sysbench` CPU benchmark was executed using a prime-number calculation limit of **20,000**.

### Key Finding

> Under the tested experimental conditions, Proxmox VE recorded **1,689.43 events/sec**, while VMware Workstation recorded **983.84 events/sec**. The measured average latency was **0.59 ms** for Proxmox VE and **1.02 ms** for VMware Workstation.

---

## Table of Contents

1. [Project Objectives](#1-project-objectives)
2. [Hypervisor Architectural Comparison](#2-hypervisor-architectural-comparison)
3. [Virtual Machine Specifications](#3-virtual-machine-specifications)
4. [Experimental Procedure](#4-experimental-procedure)
5. [Empirical Results & Screenshots](#5-empirical-results--screenshots)
6. [Performance Comparison Table](#6-performance-comparison-table)
7. [Metric Explanations & Visualizations](#7-metric-explanations--visualizations)
8. [Technical Analysis & Discussion](#8-technical-analysis--discussion)
9. [Conclusion & Engineering Takeaways](#9-conclusion--engineering-takeaways)
10. [Repository Structure & Reproduction](#10-repository-structure--reproduction)

---

## 1. Project Objectives

The primary objectives of this Cloud Computing laboratory experiment are:

1. **Deployment:** Configure Ubuntu virtual machines using two different hypervisor architectures:

   * Type-1: Proxmox VE
   * Type-2: VMware Workstation

2. **Standardization:** Use comparable virtual-machine resources:

   * 2 vCPU
   * 2 GB RAM
   * 20 GB virtual disk

3. **Benchmarking:** Execute the `sysbench` CPU benchmark using a prime-number limit of **20,000**.

4. **Metric Collection:** Record:

   * Total execution time
   * Total events
   * Events per second
   * Minimum latency
   * Average latency
   * Maximum latency

5. **Architectural Evaluation:** Compare the measured CPU performance and latency characteristics of the two virtualization environments.

---

## 2. Hypervisor Architectural Comparison

### Type-1 Hypervisor — Proxmox VE

Proxmox VE is a virtualization platform based on Linux and KVM. In the experimental setup, the Ubuntu guest virtual machine operates through the Proxmox VE/KVM virtualization layer.

```text
+-------------------------------------------------------------------+
|                 Ubuntu Virtual Machine                            |
|                                                                   |
|                 Sysbench CPU Benchmark                            |
+-------------------------------------------------------------------+
|                 Proxmox VE / KVM                                   |
|                    Type-1 Layer                                   |
+-------------------------------------------------------------------+
|                 Physical Host Hardware                             |
|                 CPU / RAM / Storage                                |
+-------------------------------------------------------------------+
```

### Type-2 Hypervisor — VMware Workstation

VMware Workstation operates as a hosted virtualization application on a host operating system. The Ubuntu guest virtual machine runs through the VMware virtualization layer.

```text
+-------------------------------------------------------------------+
|                 Ubuntu Virtual Machine                            |
|                                                                   |
|                 Sysbench CPU Benchmark                            |
+-------------------------------------------------------------------+
|                 VMware Workstation                                |
|                    Type-2 Layer                                   |
+-------------------------------------------------------------------+
|                 Host Operating System                              |
+-------------------------------------------------------------------+
|                 Physical Host Hardware                             |
|                 CPU / RAM / Storage                                |
+-------------------------------------------------------------------+
```

### Architectural Difference

| Feature              | Proxmox VE              | VMware Workstation |
| -------------------- | ----------------------- | ------------------ |
| Hypervisor Type      | Type-1                  | Type-2             |
| Virtualization Layer | Proxmox VE / KVM        | VMware Workstation |
| Host OS Dependency   | Virtualization platform | Runs on host OS    |
| Guest OS             | Ubuntu 22.04.5 LTS      | Ubuntu 22.04.5 LTS |
| CPU Benchmark        | Sysbench CPU            | Sysbench CPU       |

---

## 3. Virtual Machine Specifications

To make the benchmark comparison meaningful, the virtual machines were configured with comparable resources.

| Resource Parameter     | Proxmox VE (Type-1)       | VMware Workstation (Type-2) | Status    |
| ---------------------- | ------------------------- | --------------------------- | --------- |
| Guest Operating System | Ubuntu 22.04.5 LTS x86_64 | Ubuntu 22.04.5 LTS x86_64   | Matched   |
| CPU Allocation         | 2 vCPU                    | 2 vCPU                      | Identical |
| RAM Allocation         | 2 GB                      | 2 GB                        | Identical |
| Virtual Disk           | 20 GB                     | 20 GB                       | Identical |
| Benchmark              | `sysbench cpu`            | `sysbench cpu`              | Identical |
| CPU Prime Limit        | 20,000                    | 20,000                      | Identical |

---

## 4. Experimental Procedure

### Step 1: Virtual Machine Configuration

The virtual machines were configured using comparable resource allocations.

#### Proxmox VE

* Ubuntu 22.04.5 LTS guest
* 2 vCPU
* 2 GB RAM
* 20 GB virtual disk
* Proxmox VE / KVM virtualization

#### VMware Workstation

* Ubuntu 22.04.5 LTS guest
* 2 vCPU
* 2 GB RAM
* 20 GB virtual disk
* VMware Workstation virtualization

### Step 2: System Configuration Verification

The following commands were used inside the Ubuntu guest systems:

```bash
hostnamectl
lscpu
free -h
df -h
top
```

These commands were used to verify:

| Command       | Purpose                                    |
| ------------- | ------------------------------------------ |
| `hostnamectl` | Operating system and system information    |
| `lscpu`       | CPU architecture and processor information |
| `free -h`     | RAM and swap information                   |
| `df -h`       | Disk-space information                     |
| `top`         | Real-time system and process monitoring    |

### Step 3: Sysbench Installation

```bash
sudo apt update
sudo apt install sysbench -y
```

### Step 4: Verify Sysbench

```bash
sysbench --version
```

### Step 5: Execute CPU Benchmark

The same benchmark command was executed in both virtual machines:

```bash
sysbench cpu --cpu-max-prime=20000 run
```

The same workload was used in both environments to allow comparison of the measured performance.

---

## 5. Empirical Results & Screenshots

### Type-1 Hypervisor — Proxmox VE

#### Figure 1: Proxmox VE Dashboard

![Proxmox VE Dashboard](CC-Experiment-01-Hypervisor-Analysis/screenshots/type1-promox/01-proxmox-dashboard.png)

#### Figure 2: Proxmox VM Configuration

![Proxmox VM Configuration](CC-Experiment-01-Hypervisor-Analysis/screenshots/type1-promox/02-proxmox-vm-configuration.png)

#### Figure 3: Proxmox VM Running

![Proxmox VM Running](CC-Experiment-01-Hypervisor-Analysis/screenshots/type1-promox/03-proxmox-vm-running.png)

#### Figure 4: Proxmox Ubuntu Console

![Proxmox Ubuntu Console](CC-Experiment-01-Hypervisor-Analysis/screenshots/type1-promox/04-proxmox-ubuntu-console.png)

#### Figure 5: Proxmox System Configuration

![Proxmox System Configuration](CC-Experiment-01-Hypervisor-Analysis/screenshots/type1-promox/05-proxmox-system-configuration.png)

#### Figure 6: Proxmox Sysbench Benchmark Result

![Proxmox Sysbench Result](CC-Experiment-01-Hypervisor-Analysis/screenshots/type1-promox/06-promox-sysbench-result.png)

#### Figure 7: Proxmox Resource Monitoring

![Proxmox Resource Monitoring](CC-Experiment-01-Hypervisor-Analysis/screenshots/type1-promox/07-promox-resource-monitoring.png)

---

### Type-2 Hypervisor — VMware Workstation

#### Figure 8: VMware VM Configuration

![VMware VM Configuration](CC-Experiment-01-Hypervisor-Analysis/screenshots/type2-vmware/01-vmware-vm-configuration.png)

#### Figure 9: VMware VM Running

![VMware VM Running](CC-Experiment-01-Hypervisor-Analysis/screenshots/type2-vmware/02-vmware-vm-running.png)

#### Figure 10: VMware System Configuration

![VMware System Configuration 1](CC-Experiment-01-Hypervisor-Analysis/screenshots/type2-vmware/03-vmware-system-configuration1.png)

#### Figure 11: VMware System Configuration

![VMware System Configuration 2](CC-Experiment-01-Hypervisor-Analysis/screenshots/type2-vmware/03-vmware-system-configuration%202.png)

#### Figure 12: VMware Sysbench Benchmark Result

![VMware Sysbench Result](CC-Experiment-01-Hypervisor-Analysis/screenshots/type2-vmware/04-vmware-sysbench-result.png)

---

### Hypervisor Performance Comparison

#### Figure 13: Combined Hypervisor Performance Comparison

![Hypervisor Performance Comparison](CC-Experiment-01-Hypervisor-Analysis/screenshots/comparison/01-hypervisor-performance-comparison.png)

---

## 6. Performance Comparison Table

The following table summarizes the exact values recorded during the experimental benchmark runs.

| Performance Metric     | Proxmox VE (Type-1) | VMware Workstation (Type-2) |
| ---------------------- | ------------------: | --------------------------: |
| Hypervisor Type        |              Type-1 |                      Type-2 |
| Guest OS               |  Ubuntu 22.04.5 LTS |          Ubuntu 22.04.5 LTS |
| vCPU Allocation        |              2 vCPU |                      2 vCPU |
| RAM Allocation         |                2 GB |                        2 GB |
| Disk Capacity          |               20 GB |                       20 GB |
| CPU Prime Limit        |              20,000 |                      20,000 |
| Total Execution Time   |           10.0006 s |                   10.0010 s |
| Total Events Processed |              16,903 |                       9,842 |
| Events per Second      |            1,689.43 |                      983.84 |
| Minimum Latency        |             0.57 ms |                     0.81 ms |
| Average Latency        |             0.59 ms |                     1.02 ms |
| Maximum Latency        |             1.09 ms |                     4.38 ms |

> **Note:** A 95th-percentile latency value was not recorded in the available benchmark results and therefore is not included.

---

## 7. Metric Explanations & Visualizations

### Performance Metric Definitions

1. **Total Execution Time:** The wall-clock duration required to execute the Sysbench workload.

2. **Total Events:** The total number of benchmark operations completed during the test.

3. **Events per Second (EPS):** The number of benchmark operations completed per second. This represents the measured throughput for the workload.

4. **Latency:** The time required to complete an individual benchmark operation.

   * **Minimum Latency:** Fastest recorded operation.
   * **Average Latency:** Average time per operation.
   * **Maximum Latency:** Slowest recorded operation.

---

### Chart 1: CPU Throughput Comparison

![Events per Second Comparison](CC-Experiment-01-Hypervisor-Analysis/images/events_per_second_comparison.png)

**Figure 14:** CPU throughput comparison between Proxmox VE and VMware Workstation.

---

### Chart 2: CPU Latency Comparison

![Latency Comparison](CC-Experiment-01-Hypervisor-Analysis/images/latency_comparison.png)

**Figure 15:** Measured latency comparison between the two virtualization environments.

---

### Chart 3: Total Events Processed

![Total Events Comparison](CC-Experiment-01-Hypervisor-Analysis/images/total_events_comparison.png)

**Figure 16:** Total benchmark events completed during the test.

---

### Chart 4: Comprehensive Performance Dashboard

![Overall Performance Dashboard](CC-Experiment-01-Hypervisor-Analysis/images/overall_performance_dashboard.png)

**Figure 17:** Overall performance dashboard containing the main benchmark measurements.

---

## 8. Technical Analysis & Discussion

### 1. CPU Throughput

The Sysbench benchmark recorded:

* **Proxmox VE:** 1,689.43 events/sec
* **VMware Workstation:** 983.84 events/sec

The measured throughput differed between the two virtualization environments under the tested configuration.

### 2. Total Events

During the approximately 10-second benchmark:

* **Proxmox VE:** 16,903 events
* **VMware Workstation:** 9,842 events

The total number of completed events therefore differed between the two experimental environments.

### 3. Latency

The measured average latency was:

* **Proxmox VE:** 0.59 ms
* **VMware Workstation:** 1.02 ms

The measured maximum latency was:

* **Proxmox VE:** 1.09 ms
* **VMware Workstation:** 4.38 ms

These measurements show that the latency characteristics differed between the two tested environments.

### 4. Execution Time

The execution times were:

* **Proxmox VE:** 10.0006 seconds
* **VMware Workstation:** 10.0010 seconds

The difference in total execution time was very small because the Sysbench benchmark operated for approximately the same duration in both environments.

### 5. Factors Affecting the Results

The measured performance can be influenced by several factors:

* Hypervisor architecture
* Host operating-system overhead
* CPU scheduling
* Host background workload
* VM resource allocation
* Virtual-machine configuration
* Software configuration
* Physical hardware characteristics

Therefore, the results represent the behavior observed in this particular experimental setup and should not be treated as universal performance values for all Proxmox VE or VMware Workstation installations.

---

## 9. Conclusion & Engineering Takeaways

### Conclusion

This experiment provided a practical comparison between a Type-1 virtualization environment using Proxmox VE and a Type-2 virtualization environment using VMware Workstation.

Both environments used comparable Ubuntu virtual-machine resources and the same Sysbench CPU workload.

Under the tested conditions, differences were observed in:

* Total events
* Events per second
* Minimum latency
* Average latency
* Maximum latency

The measured execution times remained almost identical.

### Engineering Takeaways

1. **Virtualization architecture matters:** Different virtualization architectures can produce different measured performance characteristics.

2. **Resource standardization is important:** Using comparable vCPU, RAM, disk, and benchmark settings makes the comparison more meaningful.

3. **Throughput and latency provide complementary information:** Events/sec shows workload throughput, while latency describes the time taken by individual operations.

4. **Benchmark results depend on experimental conditions:** Hardware, host workload, VM configuration, and software versions can affect measured results.

5. **A benchmark should be interpreted within its scope:** The values obtained in this experiment describe the tested environment and workload rather than every possible deployment.

---

## 10. Repository Structure & Reproduction

### Folder Layout

```text
cc-records/
│
├── README.md
│
└── CC-Experiment-01-Hypervisor-Analysis/
    │
    ├── images/
    │   ├── 04-vmware-sysbench-result.png
    │   ├── 06-promox-ubantu-sysbench-result.png
    │   ├── events_per_second_comparison.png
    │   ├── latency_comparison.png
    │   ├── overall_performance_dashboard.png
    │   └── total_events_comparison.png
    │
    ├── results/
    │   └── performance-analysis.md
    │
    └── screenshots/
        │
        ├── comparison/
        │   └── 01-hypervisor-performance-comparison.png
        │
        ├── type1-promox/
        │   ├── 01-proxmox-dashboard.png
        │   ├── 02-proxmox-vm-configuration.png
        │   ├── 03-proxmox-vm-running.png
        │   ├── 04-proxmox-ubuntu-console.png
        │   ├── 05-proxmox-system-configuration.png
        │   ├── 06-promox-sysbench-result.png
        │   └── 07-promox-resource-monitoring.png
        │
        └── type2-vmware/
            ├── 01-vmware-vm-configuration.png
            ├── 02-vmware-vm-running.png
            ├── 03-vmware-system-configuration1.png
            ├── 03-vmware-system-configuration 2.png
            └── 04-vmware-sysbench-result.png
```

### How to Reproduce

#### 1. Verify the Ubuntu VM

```bash
hostnamectl
lscpu
free -h
df -h
top
```

#### 2. Install Sysbench

```bash
sudo apt update
sudo apt install sysbench -y
```

#### 3. Verify Sysbench

```bash
sysbench --version
```

#### 4. Run the Benchmark

```bash
sysbench cpu --cpu-max-prime=20000 run
```

#### 5. Record the Results

Record the following values from the Sysbench output:

* Total execution time
* Total events
* Events per second
* Minimum latency
* Average latency
* Maximum latency

---

*Laboratory Experiment conducted for Cloud Computing / Computer Networks Course.*
