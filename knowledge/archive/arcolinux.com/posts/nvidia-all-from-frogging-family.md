---
title: "Nvidia-all from Frogging Family"
url: https://arcolinux.com/nvidia-all-from-frogging-family/
date: 2024-03-22 06:38:47
type: post
categories: ["Nvidia"]
source_site: arcolinux.com
---

# Nvidia-all from Frogging Family

> <https://github.com/Frogging-Family/nvidia-all>

![](https://arcolinux.com/wp-content/uploads/2024/03/nvidia-all-.jpg)

This video outlines a detailed walkthrough of troubleshooting and setting up NVIDIA drivers on a Linux system running Wayland, specifically for an NVIDIA graphics card that is around 10 years old. The speaker discusses their experience with NVIDIA DKMS (Dynamic Kernel Module Support) and the challenges they faced while ensuring their older hardware remains supported. Here’s a concise summary:

  1. **Introduction** : The speaker begins by discussing the challenges of using NVIDIA drivers, particularly for older hardware. They highlight the importance of DKMS for maintaining driver support.
  2. **Current NVIDIA Support** : They mention using an ArcoLinuxB ISO that is close to release, indicating NVIDIA works with their current hardware setup, emphasizing the significance of having the NVIDIA DKMS.
  3. **Driver Selection and Installation** : The process involves selecting the **GeForce GTX 970** model, finding the right driver version (550.67), and then initiating the build and installation process for the NVIDIA DKMS package.
  4. **Building and Monitoring the Installation** : The speaker describes the CPU load during the build process, joking about the age of the computer. They then proceed to remove existing NVIDIA drivers and replace them with the newly built version, resolving potential conflicts with existing packages.
  5. **Conflict Resolution and Final Steps** : The installation process includes handling package conflicts and ensuring compatibility with 32-bit libraries. The speaker advises on the importance of creating a script for the installation process to streamline future setups.
  6. **Reboot and Backup** : Finally, he recommends rebooting the system and emphasize the importance of backing up data to the cloud for safety. The video concludes with the speaker pausing the recording, hoping for a successful reboot.



Throughout the walkthrough, the speaker interjects personal anecdotes and humor, making the technical process more relatable. They also stress the value of community resources, like the ArcoLinux website articles and scripts provided by the Frogging Family, for assisting with driver installation and troubleshooting.

Video: <https://youtu.be/zs6YwUBB12M>

In my latest exploration, I tackled the removal of all NVIDIA-related components to replace them with the newly built NVIDIA DKMS (Dynamic Kernel Module Support) package. Whether this adjustment offers an improvement remains to be seen, necessitating thorough testing over time.

Previously, I engaged with the Frogging Family's NVIDIA utilities, a method I suggest for those feeling lost in the maze of NVIDIA driver management. This approach involves cloning their repository, building the required software, and removing old DKMS versions in favor of the new DKG. This process, though it might seem daunting at first, is essential for ensuring that your system operates efficiently with NVIDIA hardware.

To evaluate the performance enhancements brought about by these changes, I pondered on methods to test the graphics card's capabilities. Utilizing tools like `Nvidia SMI` to monitor usage statistics is straightforward, but for a comprehensive analysis, benchmarking is key. Eventually, I found potential benchmarks like the Blender Benchmark and GPU test, yet a specific test for NVIDIA remained elusive.

Upon further research, I stumbled upon various options, including using `GLX gears` for a simple performance check. Moreover, I experimented with `GLMark 2` and `Unigine Heaven`, the latter offering a more immersive benchmarking experience, albeit with some installation and navigation challenges due to my system's age. Despite these hurdles, I achieved significant frames per second, indicating robust performance for my needs.

I must admit, as someone who isn't a gamer, my demands from a graphics setup are relatively modest. A stable, reliable display from dawn till dusk suffices. Nevertheless, this journey through driver customization and benchmarking has been enlightening. It's left me with a tailored NVIDIA driver setup, leveraging DKMS to automatically rebuild the driver with kernel updates, ensuring continued functionality without the dread of a black screen.

In conclusion, while this exploration may not revolutionize your approach to NVIDIA driver management, it has enriched my understanding and capabilities. The resulting setup, distinct from the standard ArcoLinux offering, promises to keep my decade-old GTX 970 performing smoothly across kernel updates. This endeavor not only safeguards against potential display issues but also empowers with the knowledge to maintain an aging but capable system.

Video: <https://youtu.be/YLgCkviDAm0>
