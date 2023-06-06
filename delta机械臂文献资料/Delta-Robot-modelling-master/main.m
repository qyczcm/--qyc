%% Simulate a Delta Robot mechanism

%% init
clc;
clear all;

%% Parameters
%rod length in m:
rf = 0.38;  %Base to Joint0.524 大腿
re = 0.98;  %Joint to endeffector1.244小腿

%triangular side length in m:
f =0.13;  %base0.576 大圆
e = 0.0; %endeffector0.076 小圆
param=[e,f,re,rf];
workspace(param);
%% kinematics
%actuator angles:
m=5; %number of trajectory points
n=4; %number of Poses
 
r0=[0, 0, -1.116]; %start Pose
rGoal=zeros(n+1,3);
 
%Setting goal positions
rGoal(1,:)=[-0.06558, -0.05222, -1.339];
rGoal(2,:)=r0';
rGoal(3,:)=[0.2315, -0.4401, -1.258];
rGoal(4,:)=r0';

%Initialize the matrix
trajectory=zeros(3,m,n);
angles=zeros(3,m,n);

for i=1:n
    trajectory(:,:,i)=CalcTrajectory(rGoal(i,:),rGoal(i+1,:),m);
    angles(:,:,i)=CalcTrajectoryAngles(trajectory(:,:,i),param)*pi/180;
end

%% Plot
npackages = 3; %Define the number of packages the robot wants to pick and sort
while(npackages~=0)
    for i=1:n
        Animation(angles(:,:,i),trajectory(:,:,i),param);
    end
    npackages =  npackages-1;
end






















