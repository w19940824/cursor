from dotenv import load_dotenv
import os
import sys


class Config:
    def __init__(self):
        # 获取应用程序的根目录路径
        if getattr(sys, "frozen", False):
            # 如果是打包后的可执行文件
            application_path = os.path.dirname(sys.executable)
        else:
            # 如果是开发环境
            application_path = os.path.dirname(os.path.abspath(__file__))

        # 指定 .env 文件的路径
        dotenv_path = os.path.join(application_path, ".env")

        if not os.path.exists(dotenv_path):
            raise FileNotFoundError(f"文件 {dotenv_path} 不存在")

        # 加载 .env 文件
        load_dotenv(dotenv_path)

    def get_temp_mail(self):
        return os.getenv("TEMP_MAIL")

    def get_domain(self):
        return os.getenv("DOMAIN")


# 使用示例
if __name__ == "__main__":
    try:
        config = Config()
        print("环境变量加载成功！")
        print(f"临时邮箱: {config.get_temp_mail()}")
        print(f"域名: {config.get_domain()}")
    except ValueError as e:
        print(f"错误: {e}")
