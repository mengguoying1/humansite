$images = @{
  "hero_banner.jpg" = "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/477160/255ce652883cdb8fc0dc4dac6697db71aa535f3f/ss_255ce652883cdb8fc0dc4dac6697db71aa535f3f.1920x1080.jpg"
  "mansion.jpg" = "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/477160/255ce652883cdb8fc0dc4dac6697db71aa535f3f/ss_255ce652883cdb8fc0dc4dac6697db71aa535f3f.1920x1080.jpg"
  "climbing.jpg" = "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/477160/94f4e124f87b033d985f3ff542ac8d2d7195d106/ss_94f4e124f87b033d985f3ff542ac8d2d7195d106.1920x1080.jpg"
  "factory.jpg" = "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/477160/eca0a2596d4b9e746154ee95571eb19db622e25e/ss_eca0a2596d4b9e746154ee95571eb19db622e25e.1920x1080.jpg"
  "swinging.jpg" = "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/477160/88cfb9c5b0e71d00d17310326c50c55bb4c0a77c/ss_88cfb9c5b0e71d00d17310326c50c55bb4c0a77c.1920x1080.jpg"
  "multiplayer.jpg" = "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/477160/045dbf6a11c00886d9b1fee5bd818686680463f9/ss_045dbf6a11c00886d9b1fee5bd818686680463f9.1920x1080.jpg"
  "cover.jpg" = "https://upload.wikimedia.org/wikipedia/en/e/e5/Human_Fall_Flat_cover_art.jpg"
}

foreach ($key in $images.Keys) {
  $url = $images[$key]
  $out = "static/img/$key"
  Write-Host "Downloading $url to $out ..."
  [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
  Invoke-WebRequest -Uri $url -OutFile $out -UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
Write-Host "Downloads complete."
