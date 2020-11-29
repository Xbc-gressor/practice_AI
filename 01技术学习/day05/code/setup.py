from distutils.core import setup

setup(
    name = "bigApp",
    version = "1.0",
    description = "面向对象的演示案例",
    author = "我说我这个有用",
    packages = [ #所有的包路径
        "bigApp",
        "bigAPp.ais",
        "bigAPp.uis"
    ],
    scripts = ["run_app.bat"] #{PYTHON_HOME/}
)