import pandas as pd
import numpy as np
import datetime
import os

def generate_robot_data():
    # 1. 가상의 로봇 관절 데이터 (Joint Positions) 생성
    timestamps = [datetime.datetime.now() + datetime.timedelta(milliseconds=i*100) for i in range(10)]
    joint_angles = np.random.uniform(-1.5, 1.5, size=(10, 6)) # 6축 로봇 가정
    
    df = pd.DataFrame(joint_angles, columns=[f'joint_{i+1}' for i in range(6)])
    df['timestamp'] = timestamps
    
    # 2. 데이터 저장
    os.makedirs('data', exist_ok=True)
    filename = f"data/robot_telemetry_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(filename, index=False)
    
    print(f"✅ Success: Data saved to {filename}")

if __name__ == "__main__":
    generate_robot_data()

