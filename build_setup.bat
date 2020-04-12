@echo off

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: 定义QT目录
set "QT_DIR=D:/Qt/Qt5.9.2/5.9.2/mingw53_32/bin"
set "QT_TOOLS_DIR=D:/Qt/Qt5.9.2/Tools/mingw530_32/bin"
:: 定义Inno Setup目录
set "INNO_SETUP_DIR=C:/Program Files (x86)/Inno Setup 6"
:: 定义opencv目录
set "OPENCV_DIR=D:/Qt/opencv4.2.0/x64/mingw/bin"
:: 定义版本号
set "YVYVIEWER_VERSION=0.3.4"
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: 设置环境变量
set "PATH=%QT_DIR%;%QT_TOOLS_DIR%;%INNO_SETUP_DIR%;%PATH%"
:: 编译
qmake YUVviewer.pro
mingw32-make -j8
:: clean打包目录
if exist ".\InnoSetup\build" (
    rmdir /Q /S .\InnoSetup\build
)
:: 配置打包信息
copy /y .\InnoSetup\build_setup.iss .\InnoSetup\build_temp_setup.iss
.\tools\sed\sed.exe -i "s/#define MyAppVersion \"0.3.3\"/#define MyAppVersion \"%YVYVIEWER_VERSION%\"/g" .\InnoSetup\build_temp_setup.iss
.\tools\sed\sed.exe -i "s/#define MyAppVersionInfoVersion \"0.3.3.000\"/#define MyAppVersionInfoVersion \"%YVYVIEWER_VERSION%.000\"/g" .\InnoSetup\build_temp_setup.iss
del /f /q /a .\sed*
:: 构建打包目录
xcopy /y .\build_release\out\YUVviewer.exe .\InnoSetup\build\
:: 使用windeployqt拷贝依赖dll库到打包目录
windeployqt --dir .\InnoSetup\build .\InnoSetup\build\YUVviewer.exe
xcopy /y %OPENCV_DIR%\libopencv_imgproc420.dll .\InnoSetup\build\
xcopy /y %OPENCV_DIR%\libopencv_core420.dll .\InnoSetup\build\
:: 打包
echo "wait inno build setup..."
compil32 /cc ".\InnoSetup\build_setup.iss"
del .\InnoSetup\build_temp_setup.iss
echo "build success!"
pause
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
