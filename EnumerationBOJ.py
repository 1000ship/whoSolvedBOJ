import enum

class ResultID(enum.Enum):
    ALL = -1  # 모든 결과
    SUCCESS = 4  # 맞았습니다!!
    WRONG_FORMAT = 5  # 출력 형식이 잘못되었습니다
    FAIL = 6  # 틀렸습니다
    TIME_OVER = 7  # 시간 초과
    MEMORY_OVER = 8  # 메모리 초과
    OVER_PRINTING = 9  # 출력 초과
    RUNTIME_ERROR = 10  # 런타임 에러
    COMPILE_ERROR = 11  # 컴파일 에러
    CAN_NOT_RUN = 12  # 채점 불가
    WAITING = 0  # 기다리는 중
    RETRYING = 1  # 재채점을 기다리는 중
    READY = 2  # 채점 준비 중
    TRYING = 3  # 채점 중

    @staticmethod
    def codeToMessage (code):
        dict = {
            -1: '모든 결과',
            4: '맞았습니다!!',
            5: '출력 형식이 잘못되었습니다',
            6: '틀렸습니다',
            7: '시간 초과',
            8: '메모리 초과',
            9: '출력 초과',
            10: '런타임 에러',
            11: '컴파일 에러',
            12: '채점 불가',
            0: '기다리는 중',
            1: '재채점을 기다리는 중',
            2: '채점 준비 중',
            3: '채점 중'
        }
        if code not in dict:
            return None
        return dict[code]

class LanguageID(enum.Enum):
    ALL = -1  # 모든 언어
    CPP14 = 88  # C++14
    JAVA = 3  # Java
    Python3 = 28  # Python 3
    C11 = 75  # C11
    PYPY3 = 73  # PyPy3
    C = 0  # C
    CPP = 1  # C++
    CPP11 = 49  # C++11
    CPP17 = 84  # C++17
    JAVA_OPEN_JDK = 91  # Java (OpenJDK)
    JAVA11 = 93  # Java 11
    CPP2A = 95  # C++2a
    PYTHON2 = 6  # Python 2
    PYPY2 = 32  # PyPy2
     # = 68, # Ruby 2.7
     # = 69, # Kotlin (JVM)
     # = 92, # Kotlin (Native)
     # = 74, # Swift
     # = 58, # Text
     # = 62, # C# 6.0
     # = 17, # node.js
     # = 12, # Go
     # = 29, # D
     # = 100, # D (LDC)
     # = 37, # F#
     # = 7, # PHP
     # = 44, # Rust
     # = 94, # Rust 2018
     # = 2, # Pascal
     # = 16, # Lua
     # = 8, # Perl
     # = 72, # R
     # = 10, # Objective-C
     # = 64, # Objective-C++
     # = 59, # C (Clang)
     # = 60, # C++ (Clang)
     # = 66, # C++11 (Clang)
     # = 67, # C++14 (Clang)
     # = 77, # C11 (Clang)
     # = 85, # C++17 (Clang)
     # = 96, # C++2a (Clang)
     # = 79, # Golfscript
     # = 27, # Assembly (32bit)
     # = 87, # Assembly (64bit)
     # = 63, # VB.NET 4.0
     # = 5, # Bash
     # = 13, # Fortran
     # = 14, # Scheme
     # = 19, # Ada
     # = 21, # awk
     # = 22, # OCaml
     # = 23, # Brainf**k
     # = 24, # Whitespace
     # = 26, # Tcl
     # = 34, # Rhino
     # = 35, # Cobol
     # = 41, # Pike
     # = 43, # sed
     # = 46, # Boo
     # = 47, # INTERCAL
     # = 48, # bc
     # = 54, # Cobra
     # = 70, # Algol 68
     # = 71, # Befunge
     # = 81, # Haxe
     # = 82, # LOLCODE
     # = 83, # 아희
     # = 99, # Minecraft