close all; clear; clc

% Get data
data_loaded = load('output.dat');
% Sort from lower to higher on x-axis
datas = sortrows(data_loaded,1);
[C,ia,idx] = unique(datas(:,1),'stable');
val = accumarray(idx,datas(:,2),[],@mean); 
smoothed_data = [C val];
%smoothed_data = smoothdata(datas,2,'rlowess');

plot(smoothed_data(:,1),smoothed_data(:,2),'LineWidth',2);