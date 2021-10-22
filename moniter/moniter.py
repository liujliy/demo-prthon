import psutil
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

fig, ax = plt.subplots()

ax.set_ylim([0, 100])
ax.set_xlim([0, 100])
ax.set_autoscale_on(False)
ax.set_xticks([])
ax.set_yticks(range(0, 101, 10))
ax.grid(True)

# CPU使用率
cpu_data = [None] * 100
# 内存使用率
mem_data = [None] * 100
# 磁盘使用率（这个方法有问题）
disk_data = [None] * 100
# 标签
l_cpu, = ax.plot(range(100), cpu_data, label='CPU %')
l_mem, = ax.plot(range(100), mem_data, label='MEM %')
l_disk, = ax.plot(range(100), disk_data, label = 'DISK %')
ax.legend(loc='upper center', ncol=4, prop=font_manager.FontProperties(size=10))

def monitor(ax):
    global cpu_data, mem_data, disk_data
    cpu_data = cpu_data[1:] + [psutil.cpu_percent()]
    mem_data = mem_data[1:] + [psutil.virtual_memory().percent]
    disk_data = disk_data[1:] + [psutil.disk_usage("C:\\").percent]
    l_cpu.set_ydata(cpu_data)
    l_mem.set_ydata(mem_data)
    l_disk.set_ydata(disk_data)
    ax.draw_artist(l_cpu)
    ax.draw_artist(l_mem)
    ax.draw_artist(l_disk)
    ax.figure.canvas.draw()

timer = fig.canvas.new_timer(interval=100)
timer.add_callback(monitor, ax)
timer.start()
plt.show()
