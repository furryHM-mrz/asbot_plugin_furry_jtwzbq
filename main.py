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

@register("asbot_plugin_furry_jtwzbq", "furryhm", "正则表达式文字表情发送", "2.0.0")
class FurryEmojiPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.keyword_pairs = []
        self.compiled_patterns = []  # 存储编译后的正则表达式

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
                
            # 编译正则表达式模式以提高性能
            self.compiled_patterns = []
            for pair in self.keyword_pairs:
                pattern = re.compile(pair['trigger'])
                self.compiled_patterns.append({
                    'pattern': pattern,
                    'trigger': pair['trigger'],
                    'response': pair['response']
                })
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
        
        # 使用正则表达式匹配触发词
        for pattern_info in self.compiled_patterns:
            if pattern_info['pattern'].fullmatch(text.strip()):
                logger.debug(f"正则匹配到触发词: {pattern_info['trigger']}")
                return event.plain_result(pattern_info['response'])
            else:
                logger.debug(f"未匹配到触发词: {text.strip()}")
            
        return None

    async def terminate(self): 
        pass