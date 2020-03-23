## 适用于 Arch Linux 的 Calamares 配置档

> 由于已知问题较多，请不要在非测试环境中使用本配置档。

## 依赖
在 Archiso 配置档 `packages.x86_64` 下加入：

```
kf5
qt5
boost
kpmcore
yaml-cpp
polkit-qt5
```

## 部署
将目录中的文件放入 Archiso 配置档 `airootfs/root` 中，在构建镜像时可使用 `airootfs/root/customize_airootfs.sh` 调用 `airootfs/root/build_calamares.sh`。

特别地：`pacstrap_calamares` 应放置在 `airootfs/usr/bin/pacstrap_calamares`，在用户安装过程中由 Calamares 的 `pacstrap ` 模组调用。
