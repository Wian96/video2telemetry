close all; clear; clc

%% GENERATE THE tmp DIRECTORY

mkdir __tmp_img__
mkdir __dat_out__

%% RUN THE ITERATION ON THE VIDEO

vid = VideoReader('video.mp4');
len = vid.Duration; % Get video length
width = vid.Width; % Get video width
height = vid.Height; % Get video height
fr = vid.FrameRate; % Get framerate
% Intialize the time vector based on video length
time_vect = linspace(0,len,len*fr);

for ii = 1:length(time_vect)
    vid.CurrentTime = ii; %Suppose We have a 50 s video, by using this command we can set at 36 seconds. 
    vidFrame = read(vid,ii); %This extract the exact frame of the video (in our case a graph at a specific point) 
    out_str = ['__tmp_img__\frame_'+string(ii)+'.png'];
    imwrite(vidFrame,out_str);
    % Run python function
    pyrunfile('__main__.py',out_str);
end
% Get data
data_loaded = load('output.dat');
% Sort from lower to higher on x-axis
datas = sortrows(data_loaded,1);
[C,ia,idx] = unique(datas(:,1),'stable');
val = accumarray(idx,datas(:,2),[],@mean); 
smoothed_data = [C val];
%smoothed_data = smoothdata(datas,2,'rlowess');

plot(smoothed_data(:,1),smoothed_data(:,2),'LineWidth',2);