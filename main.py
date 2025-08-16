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

@register("asbot_plugin_furry_jtwzbq", "furryhm", "监听文字表情时重复发送", "1.2.0")
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
        except Exception as e:
            logger.error(f"加载配置文件时出错: {e}")


    @event_message_type(EventMessageType.ALL)
    async def on_message(self, event: AstrMessageEvent) -> MessageEventResult:
        """
        处理所有消息事件，检查关键词并回复
        """
        msg_obj = event.message_obj
        text = msg_obj.message_str or ""
        
        # 添加调试日志，查看消息发送者信息
        logger.debug(f"收到消息: {text}, 发送者: {msg_obj.sender}")
        
        # 只有当文本完全匹配触发词时才回复
        if text.strip() in self.trigger_map:
            logger.debug(f"匹配到触发词: {text.strip()}")
            return event.plain_result(self.trigger_map[text.strip()])
        else:
            logger.debug(f"未匹配到触发词: {text.strip()}")
            
        return None

    async def terminate(self): 
        pass