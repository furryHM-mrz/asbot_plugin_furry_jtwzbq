# asbot_plugin_furry_jtwzbq

![版本](https://img.shields.io/badge/version-2.0.0-blue)
![AstrBot](https://img.shields.io/badge/AstrBot-plugin-green)

正则表达式文字表情发送插件

## 功能介绍

这是一个为AstrBot平台开发的插件，可以根据用户发送的特定关键词自动回复预设的文字表情。插件使用正则表达式完全匹配的方式触发回复，确保只在精确匹配时才会响应。

例如：
- 发送 `awa` 会回复 `qwq`
- 发送 `qwq` 会回复 `awa`
- 发送 `uwu` 会回复 `QAQ`

## 表情映射表

插件内置了丰富的文字表情映射，包括但不限于：

| 触发词 | 回复内容 |
|--------|---------|
| awa | qwq |
| qwq | awa |
| uwu | QAQ |
| QAQ | uwu |
| owo | xwx |
| sws | zwz |
| xwx | owo |
| zwz | sws |
| hwh | xvx |
| xvx | hwh |
| ywy | zaz |
| zaz | ywy |
| mwm | nwn |
| nwn | mwm |
| qvq | pwp |
| pwp | qvq |
| 666 | 6969 |
| 6969 | 666 |
| Orz | OvO |
| OvO | Orz |
| XD | DX |
| DX | XD |
| 中 | 太中嘞 |
| 太中嘞 | 中 |
| 俺不中嘞 | 不中 |
| 不中 | 俺不中嘞 |
| >_< | o_o |
| o_o | >_< |
| 0w0 | 0v0 |
| 0v0 | 0w0 |
| @_@ | #_# |
| #_# | @_@ |
| *_* | &_& |
| &_& | *_* |
| 好色 | 喜欢~ |
| 好涩 | 喜欢~ |
| 嗷呜 | 呜嗷 |
| 呜嗷 | 嗷呜 |
| 毛毛 | 爪爪 |
| 爪爪 | 毛毛 |
| 臭臭的 | 尾巴 |
| 吸烟 | 唔!烟,吸烟?不准! |
| ? | 脑子里只剩问号惹~ |

## 配置文件

插件使用 [config.yaml](config.yaml) 文件来定义关键词映射关系。您可以根据需要修改或添加新的关键词对：

```yaml
keywords:
  - trigger: "触发词"
    response: "回复内容"
    
  - trigger: "另一个触发词"
    response: "对应的回复内容"
```

配置文件使用YAML格式，每个关键词对包含：
- `trigger`: 触发词（用户发送的内容）
- `response`: 回复内容（机器人回复的内容）

修改配置文件后需要重启插件才能生效。

## 使用说明

1. 当用户发送的消息完全匹配某个触发词时，插件会自动回复对应的内容
2. 匹配方式为正则表达式的完全匹配（fullmatch），即整个消息内容必须与触发词完全一致才会触发
3. 如果有多个匹配项，插件会随机选择其中一个进行回复
4. 插件对大小写敏感，`Awa` 和 `awa` 被视为不同的触发词

## 开发信息

- **插件名称**: asbot_plugin_furry_jtwzbq
- **作者**: furryhm
- **版本**: 2.0.0
- **仓库地址**: [https://github.com/furryHM-mrz/asbot_plugin_furry_jtwzbq](https://github.com/furryHM-mrz/asbot_plugin_furry_jtwzbq)

## 更新日志

- **v2.0.0**: 使用正则表达式完全匹配方式替代之前的简单包含判断，提高匹配准确性
- **早期版本**: 基础功能实现和关键词配置

## 联系方式

如有问题或建议，请联系QQ: 3322969592