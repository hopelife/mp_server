from setuptools import setup
import mp_server

setup(
    name='mp_server',
    version=mp_server.__version__,
    description='Moon Package for Server(flask, django, dash, graphql, ...)',
    url='https://github.com/hopelife/mp_server',
    author='Moon Jung Sam',
    author_email='monblue@snu.ac.kr',
    license='MIT',
    packages=['mp_server'],
    # entry_points={'console_scripts': ['mp_server = mp_server.__main__:main']},
    keywords='backend server',
    # python_requires='>=3.8',  # Python 3.8.6-32 bit
    # install_requires=[ # 패키지 사용을 위해 필요한 추가 설치 패키지
    #     'selenium',
    # ],
    # zip_safe=False
)
