# superset_config.py
import datetime

import jwt

# ================= 内嵌安全配置 =================
FEATURE_FLAGS = {
    # 允许仪表板直接通过URL访问（无需登录）
    "EMBEDDED_SUPERSET": True,

    # 启用公共角色访问
    # "PUBLIC_ROLE_LIKE_GAMMA": True
}
# EMBEDDED_SUPERSET = True
# ENABLE_TEMPLATE_PROCESSING = True

# 允许跨域（CORS配置）
ENABLE_CORS = True
CORS_OPTIONS = {
    "supports_credentials": False,
    # "supports_credentials": True,
    "allow_headers": ["*"],
    "resources": ["*"],
    "origins": ["http://localhost:3000", "https://your-domain.com", "http://localhost:5173", "http://127.0.0.1:8088"]  # 你的前端域名
    # "origins": ["*"]  # 你的前端域名
}


# 禁用X-Frame-Options以允许iframe嵌入
TALISMAN_CONFIG = {
    "content_security_policy": {
        "default-src": ["'self'", "'unsafe-inline'", "'unsafe-eval'", "*"],
        # "frame-ancestors": ["'self'", "http://localhost:3000", "https://your-domain.com", "http://localhost:5173"]
        "frame-ancestors": ["'self'", "*"]
    },
    "force_https": False,
    "session_cookie_secure": False
}


# 禁用CSRF保护（仅限开发环境）
WTF_CSRF_ENABLED = False

# 允许公共角色访问的数据库和数据集
# PUBLIC_ROLE_LIKE = "Gamma"
# PUBLIC_ACCESS_ROLE_LIKE = "Gamma"
# PUBLIC_ROLE_LIKE = "Public"
# PUBLIC_ACCESS_ROLE_LIKE = "Public"


GUEST_TOKEN_JWT_EXP_SECONDS = 30000  # 5 minutes
JWT_VERIFY_SUB = False



# import logging
# from logging.handlers import RotatingFileHandler
#
# # 自定义日志目录（示例路径）
# LOG_DIRECTORY = "/Users/hc/Desktop/my_app_data/superset/logs"
#
# # 基础日志配置（覆盖 Superset 默认配置）
# def configure_logging():
#     # 确保目录存在
#     import os
#     os.makedirs(LOG_DIRECTORY, exist_ok=True)
#
#     # 配置日志格式
#     formatter = logging.Formatter(
#         "%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d ▶ %(message)s"
#     )
#
#     # 添加 RotatingFileHandler（按大小轮转）
#     file_handler = RotatingFileHandler(
#         filename=f"{LOG_DIRECTORY}/superset.log",
#         maxBytes=100 * 1024 * 1024,  # 100MB
#         backupCount=5,
#         encoding="utf-8",
#     )
#     file_handler.setFormatter(formatter)
#     # file_handler.setLevel(logging.INFO)  # 设置日志级别
#     file_handler.setLevel(logging.DEBUG)  # 设置日志级别
#
#     # 清空现有 Handler 并添加自定义Handler
#     root_logger = logging.getLogger()
#     root_logger.handlers.clear()
#     root_logger.addHandler(file_handler)
#
# # 调用配置函数（Superset 初始化时会加载）
# configure_logging()

print("✅ Superset config loaded successfully!")
