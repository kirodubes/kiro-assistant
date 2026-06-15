---
title: "Fix for hanging loading location data screen in calamares"
url: https://arcolinux.com/fix-for-hanging-loading-location-data-screen-in-calamares/
date: 2019-02-05 14:36:17
type: post
categories: ["Fixes"]
source_site: arcolinux.com
---

# Fix for hanging loading location data screen in calamares

![](https://arcolinux.com/wp-content/uploads/2019/02/loading-location-data-calamares.jpg)

During the installation Calamares tries to make contact with a server to know your timezone.

Calamares checks your timezone with this code (February 2019).
    
    
    ---
    region: "America"
    zone: "New_York"
    
    # GeoIP settings. Leave commented out to disable GeoIP.
    localeGenPath: "/etc/locale.gen"
    geoipUrl:      "https://geoip.kde.org/v1/calamares"
    geoipStyle: "json"
    geoipSelector: "time_zone"

Calamares tries to make contact with a specific url

[**https://geoip.kde.org/v1/calamares**](<https://geoip.kde.org/v1/calamares>)

But sometimes the service is offline (maintenance or other reasons).

You can interrupt this automatic search and set the timezone yourself with this easy trick.

**Disable the networking via the network icon in system panel.**

**Set your timezone manually.**

**Enable the networking again via the network icon in system panel.**

Video: <https://www.youtube.com/watch?v=6OeNpUb27os>
