from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("asbot_plugin_furry_jtwzbq", "furryhm", "监听文字表情时重复发送", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
    
    # 监听文本消息，当消息内容为awa时触发
    @filter.command("awa")  # 筛选文本内容为awa的消息
    async def reply_awa(self, event: AstrMessageEvent):
        """监听到awa时回复awa"""
        # 直接回复固定文本"awa"
        yield event.plain_result("awa")

    # 监听文本消息，当消息内容为qwq时触发
    @filter.command("qwq")  # 筛选文本内容为qwq的消息
    async def reply_qwq(self, event: AstrMessageEvent):
        """监听到qwq时回复qwq"""
        # 直接回复固定文本"qwq"
        yield event.plain_result("qwq")

    # 监听文本消息，当消息内容为uwu时触发
    @filter.command("uwu")
    async def reply_uwu(self, event: AstrMessageEvent):
        """监听到uwu时回复uwu"""
        # 直接回复固定文本"uwu"
        yield event.plain_result("uwu")

    # 监听文本消息以此类推，懒得写注释。
    @filter.command("QAQ")
    async def reply_QAQ(self, event: AstrMessageEvent):
        yield event.plain_result("QAQ")

    @filter.command("owo")
    async def reply_owo(self, event: AstrMessageEvent):
        yield event.plain_result("owo")

    @filter.command("sws")
    async def reply_sws(self, event: AstrMessageEvent):
        yield event.plain_result("sws")

    @filter.command("xwx")
    async def reply_xwx(self, event: AstrMessageEvent):
        yield event.plain_result("xwx")

    @filter.command("owo")
    async def reply_owo(self, event: AstrMessageEvent):
        yield event.plain_result("owo")

    @filter.command("zwz")
    async def reply_zwz(self, event: AstrMessageEvent):
        yield event.plain_result("zwz")

    @filter.command("hwh")
    async def reply_hwh(self, event: AstrMessageEvent):
        yield event.plain_result("hwh")

    @filter.command("xvx")
    async def reply_xvx(self, event: AstrMessageEvent):
        yield event.plain_result("xvx")

    async def terminate(self): 
          pass