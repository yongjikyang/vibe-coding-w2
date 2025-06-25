#!/usr/bin/env python3
"""
간단한 버그 테스트 스크립트
"""

import sys
import os

# backend 경로 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

def test_config_bug():
    """config.py의 PORT 설정 버그 테스트"""
    try:
        from app.config import settings
        print(f"✅ SUCCESS: PORT = {settings.PORT}")
        return True
    except Exception as e:
        print(f"❌ ERROR: {type(e).__name__}: {str(e)}")
        return False

if __name__ == "__main__":
    print("🧪 Config 버그 테스트 시작...")
    success = test_config_bug()
    
    if not success:
        print("\n💥 버그 발견! 테스트 실패")
        sys.exit(1)
    else:
        print("\n✅ 테스트 통과")
        sys.exit(0) 