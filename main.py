import logging
import random
import requests
from astrbot.api.star import Context, Star, register
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.event.filter import event_message_type, EventMessageType
import re
import yaml
import os

logger = logging.getLogger(__name__)

@register("asbot_plugin_furry_jtwzbq", "furryhm", "监听文字表情时重复发送", "1.0.0")
class FurryEmojiPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.keyword_pairs = []
        self.trigger_map = {}  #创建触发词到回复的映射字典

    async def initialize(self):
        """加载配置文件"""
        self.load_config()

    def load_config(self):
        """加载配置文件"""
        config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
                self.keyword_pairs = config.get('keywords', [])
                
            #创建触发词到回复的映射字典，提高查找效率,懒得写自己品了
            self.trigger_map = {pair['trigger']: pair['response'] for pair in self.keyword_pairs}
            logger.info(f"成功加载 {len(self.keyword_pairs)} 对关键词配置")
        except FileNotFoundError:
            logger.warning("配置文件未找到，使用默认配置")
            self.set_default_config()
        except Exception as e:
            logger.error(f"加载配置文件时出错: {e}")
            self.set_default_config()

    def set_default_config(self):
        """设置默认配置"""
        self.keyword_pairs = [
            {"trigger": "awa", "response": "qwq"},
            {"trigger": "qwq", "response": "awa"},
            {"trigger": "uwu", "response": "QAQ"},
            {"trigger": "QAQ", "response": "uwu"},
            {"trigger": "owo", "response": "xwx"},
            {"trigger": "sws", "response": "zwz"},
            {"trigger": "xwx", "response": "owo"},
            {"trigger": "zwz", "response": "sws"},
            {"trigger": "hwh", "response": "xvx"},
            {"trigger": "xvx", "response": "hwh"},
            {"trigger": "ywy", "response": "zaz"},
            {"trigger": "zaz", "response": "ywy"},
            {"trigger": "mwm", "response": "nwn"},
            {"trigger": "nwn", "response": "mwm"}
        ]
        self.trigger_map = {pair['trigger']: pair['response'] for pair in self.keyword_pairs}

    @event_message_type(EventMessageType.ALL)
    async def on_message(self, event: AstrMessageEvent) -> MessageEventResult:
        """
        处理所有消息事件，检查关键词并回复
        """
        msg_obj = event.message_obj
        text = msg_obj.message_str or ""
        
        for trigger, response in self.trigger_map.items():
            if trigger in text:
                return event.plain_result(response)
        
        if "qwq" in text:
            return event.plain_result("qwq")
            
        return event.continue_result()


    async def terminate(self): 
        pass
