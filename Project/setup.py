#coding:utf-8

try:
    # pip 版本 < 10
    from pip.req import parse_requirements
except ImportError:
    # pip 版本 >= 10
    from pip._internal.req import parse_requirements

from setuptools import find_packages, setup

# 读取外部文件，获取版本号
with open("./VERSION.txt", "r") as f:
    version = f.read().strip()

# 读取外部文件，获取运行依赖项
def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


setup(
    name='scrapy-plus',  # 模块名称
    version=version,    # 版本号
    description='A mini spider framework, like Scrapy',  # 描述
    packages=find_packages(exclude=[]), # 打包文件排除的文件，当前没有排除文件
    author='itcast',
    author_email='your@email.com',
    license='Apache License v2',  # 遵循的发行许可证，GPL、APL、BSD  （加州大学伯克利分校）
    package_data={'': ['*.*']},   # 导入所有文件做为包数据
    url='#',
    install_requires=parse_requirements("requirements.txt"),  # 所需的运行环境
    zip_safe=False, # 在Windows下卸载不报错
    # 分类数据
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

