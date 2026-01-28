#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clinker GUI - Gene Cluster Comparison Visualization Tool
A modern GUI interface for the clinker command-line tool

基因簇比对可视化工具图形界面
为 clinker 命令行工具提供现代化的 GUI 界面

Author: Antigravity AI Assistant
Date: 2026-01-28
Version: 2.0 (International Edition)
"""

import os
import sys
import subprocess
import threading
import webbrowser
import locale
from datetime import datetime
from pathlib import Path
from tkinter import filedialog, messagebox
import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD

# ============================================================================
# 环境配置：修复 Windows 编码问题 / Environment Configuration
# ============================================================================
os.environ["PYTHONUTF8"] = "1"  # 强制 UTF-8 编码，解决 GBK/UTF-8 冲突

# ============================================================================
# GUI 主题配置 / GUI Theme Configuration
# ============================================================================
ctk.set_appearance_mode("dark")  # 深色模式 / Dark mode
ctk.set_default_color_theme("blue")  # 蓝色主题 / Blue theme

# ============================================================================
# 国际化语言配置 / Internationalization Language Configuration
# ============================================================================

LANGUAGES = {
    'zh_CN': {
        # 窗口标题
        'window_title': 'Clinker GUI - 基因簇比对可视化工具',
        
        # 菜单和按钮
        'language': '语言',
        'chinese': '中文',
        'english': 'English',
        
        # 文件选择区
        'input_files': '📁 输入文件',
        'drag_hint': '🖱️ 拖拽文件到这里\n或点击下方按钮浏览',
        'browse_files': '📂 浏览文件',
        'selected_files': '已选文件列表:',
        'remove_selected': '❌ 删除选中',
        'clear_list': '🗑️ 清空列表',
        
        # 参数配置
        'parameters': '⚙️ 参数配置',
        'identity': '序列一致性 (Identity):',
        'output_filename': '输出文件名:',
        'output_directory': '输出目录:',
        'auto_directory': '（自动使用第一个文件的目录）',
        'advanced_options': '▶ 高级选项',
        'advanced_options_open': '▼ 高级选项',
        'no_align': '不对齐聚类 (--no_align)',
        'use_file_order': '按文件顺序显示 (--use_file_order)',
        'hide_link_headers': '隐藏链接标题 (--hide_link_headers)',
        'hide_aln_headers': '隐藏对齐标题 (--hide_aln_headers)',
        'force_overwrite': '覆盖已有文件 (--force)',
        
        # 执行控制
        'execution_control': '🚀 执行控制',
        'start_analysis': '▶️ 开始分析',
        'running': '⏳ 运行中...',
        'run_log': '📋 运行日志',
        'clear_log': '🗑️ 清空日志',
        'open_result': '📊 打开结果',
        
        # 日志信息
        'welcome': '欢迎使用 Clinker GUI！',
        'welcome_hint': '请添加 .gbk 或 .gb 格式的基因组文件开始分析。',
        'files_added': '添加了 {} 个文件',
        'files_dropped': '拖拽添加了 {} 个文件',
        'no_files_added': '⚠️ 未添加任何文件（仅支持 .gbk, .gb, .gff3 格式）',
        'file_removed': '删除了文件: {}',
        'files_cleared': '清空了 {} 个文件',
        'output_dir_set': '输出目录已设置: {}',
        'start_execution': '🚀 开始执行 Clinker 分析...',
        'command': '命令: {}',
        'analysis_complete': '✅ 分析完成！',
        'result_file': '结果文件: {}',
        'analysis_failed': '❌ 分析失败！退出代码: {}',
        'clinker_not_found': '❌ 错误: 未找到 clinker 命令！',
        'clinker_install_hint': '请确保 clinker 已正确安装并在系统 PATH 中。',
        'execution_error': '❌ 执行错误: {}',
        'result_opened': '已在浏览器中打开结果文件: {}',
        'error_info': '⚠️ 错误信息:',
        
        # 对话框
        'error': '错误',
        'warning': '警告',
        'success': '成功',
        'no_input_files': '请至少添加一个输入文件！',
        'task_running': '已有任务正在运行，请等待完成！',
        'command_build_failed': '构建命令失败: {}',
        'analysis_complete_dialog': 'Clinker 分析已完成！\n\n结果文件:\n{}\n\n是否立即打开结果？',
        'analysis_failed_dialog': 'Clinker 执行失败，请查看日志了解详情。',
        'cannot_open_file': '无法打开结果文件: {}',
        'file_not_exists': '结果文件不存在或尚未生成！',
        'select_genome_files': '选择基因组文件',
        'select_output_dir': '选择输出目录',
    },
    
    'en_US': {
        # Window title
        'window_title': 'Clinker GUI - Gene Cluster Comparison Tool',
        
        # Menu and buttons
        'language': 'Language',
        'chinese': '中文',
        'english': 'English',
        
        # File selection area
        'input_files': '📁 Input Files',
        'drag_hint': '🖱️ Drag files here\nor click button below to browse',
        'browse_files': '📂 Browse Files',
        'selected_files': 'Selected Files:',
        'remove_selected': '❌ Remove Selected',
        'clear_list': '🗑️ Clear List',
        
        # Parameters
        'parameters': '⚙️ Parameters',
        'identity': 'Sequence Identity:',
        'output_filename': 'Output Filename:',
        'output_directory': 'Output Directory:',
        'auto_directory': '(Auto: first file directory)',
        'advanced_options': '▶ Advanced Options',
        'advanced_options_open': '▼ Advanced Options',
        'no_align': 'Do not align clusters (--no_align)',
        'use_file_order': 'Use file order (--use_file_order)',
        'hide_link_headers': 'Hide link headers (--hide_link_headers)',
        'hide_aln_headers': 'Hide alignment headers (--hide_aln_headers)',
        'force_overwrite': 'Force overwrite (--force)',
        
        # Execution control
        'execution_control': '🚀 Execution Control',
        'start_analysis': '▶️ Start Analysis',
        'running': '⏳ Running...',
        'run_log': '📋 Run Log',
        'clear_log': '🗑️ Clear Log',
        'open_result': '📊 Open Result',
        
        # Log messages
        'welcome': 'Welcome to Clinker GUI!',
        'welcome_hint': 'Please add .gbk or .gb genome files to start analysis.',
        'files_added': 'Added {} file(s)',
        'files_dropped': 'Dropped {} file(s)',
        'no_files_added': '⚠️ No files added (only .gbk, .gb, .gff3 supported)',
        'file_removed': 'Removed file: {}',
        'files_cleared': 'Cleared {} file(s)',
        'output_dir_set': 'Output directory set: {}',
        'start_execution': '🚀 Starting Clinker analysis...',
        'command': 'Command: {}',
        'analysis_complete': '✅ Analysis complete!',
        'result_file': 'Result file: {}',
        'analysis_failed': '❌ Analysis failed! Exit code: {}',
        'clinker_not_found': '❌ Error: clinker command not found!',
        'clinker_install_hint': 'Please ensure clinker is installed and in system PATH.',
        'execution_error': '❌ Execution error: {}',
        'result_opened': 'Opened result file in browser: {}',
        'error_info': '⚠️ Error information:',
        
        # Dialogs
        'error': 'Error',
        'warning': 'Warning',
        'success': 'Success',
        'no_input_files': 'Please add at least one input file!',
        'task_running': 'A task is already running, please wait!',
        'command_build_failed': 'Failed to build command: {}',
        'analysis_complete_dialog': 'Clinker analysis completed!\n\nResult file:\n{}\n\nOpen result now?',
        'analysis_failed_dialog': 'Clinker execution failed. Please check the log for details.',
        'cannot_open_file': 'Cannot open result file: {}',
        'file_not_exists': 'Result file does not exist or has not been generated!',
        'select_genome_files': 'Select Genome Files',
        'select_output_dir': 'Select Output Directory',
    }
}


def detect_system_language():
    """检测系统语言 / Detect system language"""
    try:
        # 获取系统语言设置
        system_lang = locale.getdefaultlocale()[0]
        if system_lang:
            # 中文系统
            if system_lang.startswith('zh'):
                return 'zh_CN'
            # 其他系统默认英文
            else:
                return 'en_US'
    except:
        pass
    # 默认英文
    return 'en_US'


class ClinkerGUI(ctk.CTk, TkinterDnD.DnDWrapper):
    """Clinker GUI 主窗口类 / Clinker GUI Main Window Class"""
    
    def __init__(self):
        super().__init__()
        self.TkdndVersion = TkinterDnD._require(self)
        
        # 语言设置 / Language settings
        self.current_language = detect_system_language()
        
        # 窗口基础配置 / Window basic configuration
        self.title(self.t('window_title'))
        self.geometry("1100x750")
        # 移除最小窗口尺寸限制，改用滚动条支持
        self._center_window()
        
        # 数据存储 / Data storage
        self.file_paths = []  # 存储所有输入文件的绝对路径
        self.output_file_path = None  # 存储生成的结果文件路径
        self.is_running = False  # 标记是否正在运行
        
        # 创建 GUI 界面 / Create GUI interface
        self._create_widgets()
        
    def t(self, key):
        """获取当前语言的文本 / Get text in current language"""
        return LANGUAGES[self.current_language].get(key, key)
    
    def switch_language(self, lang_code):
        """切换语言并刷新界面 / Switch language and refresh GUI"""
        if lang_code != self.current_language:
            self.current_language = lang_code
            self._refresh_ui()
    
    def _refresh_ui(self):
        """刷新所有UI文本 / Refresh all UI texts"""
        # 更新窗口标题
        self.title(self.t('window_title'))
        
        # 更新所有标签和按钮
        try:
            self.file_label.configure(text=self.t('input_files'))
            self.drop_label.configure(text=self.t('drag_hint'))
            self.browse_btn.configure(text=self.t('browse_files'))
            self.list_label.configure(text=self.t('selected_files'))
            self.remove_btn.configure(text=self.t('remove_selected'))
            self.clear_btn.configure(text=self.t('clear_list'))
            
            self.param_label.configure(text=self.t('parameters'))
            self.identity_label_text.configure(text=self.t('identity'))
            self.output_name_label.configure(text=self.t('output_filename'))
            self.output_dir_label.configure(text=self.t('output_directory'))
            
            # 更新高级选项按钮文本
            if self.advanced_visible:
                self.advanced_btn.configure(text=self.t('advanced_options_open'))
            else:
                self.advanced_btn.configure(text=self.t('advanced_options'))
            
            self.no_align_cb.configure(text=self.t('no_align'))
            self.use_file_order_cb.configure(text=self.t('use_file_order'))
            self.hide_link_cb.configure(text=self.t('hide_link_headers'))
            self.hide_aln_cb.configure(text=self.t('hide_aln_headers'))
            self.force_cb.configure(text=self.t('force_overwrite'))
            
            self.control_label.configure(text=self.t('execution_control'))
            if self.is_running:
                self.run_btn.configure(text=self.t('running'))
            else:
                self.run_btn.configure(text=self.t('start_analysis'))
            
            self.log_label.configure(text=self.t('run_log'))
            self.clear_log_btn.configure(text=self.t('clear_log'))
            self.open_result_btn.configure(text=self.t('open_result'))
        except AttributeError:
            # 初始化时某些组件可能还不存在
            pass
    
    def _center_window(self):
        """将窗口居中显示 / Center the window"""
        self.update_idletasks()
        width = 1100
        height = 750
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
    
    def _create_widgets(self):
        """创建所有 GUI 组件 / Create all GUI components"""
        
        # ====================================================================
        # 顶部菜单栏：语言切换 / Top menu bar: Language switcher
        # ====================================================================
        top_frame = ctk.CTkFrame(self, height=40, fg_color="transparent")
        top_frame.pack(side="top", fill="x", padx=10, pady=(5, 0))
        
        # 语言标签和下拉菜单
        lang_label = ctk.CTkLabel(top_frame, text=self.t('language') + ":", 
                                   font=ctk.CTkFont(size=12))
        lang_label.pack(side="left", padx=(0, 5))
        
        self.lang_menu = ctk.CTkOptionMenu(
            top_frame,
            values=[self.t('chinese'), self.t('english')],
            command=self._on_language_change,
            width=100,
            font=ctk.CTkFont(size=12)
        )
        # 设置默认值
        if self.current_language == 'zh_CN':
            self.lang_menu.set(LANGUAGES['zh_CN']['chinese'])
        else:
            self.lang_menu.set(LANGUAGES['en_US']['english'])
        
        self.lang_menu.pack(side="left")
        
        # ====================================================================
        # 左侧面板：文件选择和参数配置（使用可滚动框架）
        # ====================================================================
        # 创建左侧容器框架
        left_container = ctk.CTkFrame(self, width=420)
        left_container.pack(side="left", fill="both", padx=10, pady=10)
        left_container.pack_propagate(False)
        
        # 使用可滚动框架包裹所有左侧内容
        left_frame = ctk.CTkScrollableFrame(
            left_container,
            width=380,
            fg_color="transparent"
        )
        left_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # --- 文件选择区 ---
        self.file_label = ctk.CTkLabel(left_frame, text=self.t('input_files'), 
                                   font=ctk.CTkFont(size=16, weight="bold"))
        self.file_label.pack(pady=(10, 5))
        
        # 拖拽提示区域
        self.drop_label = ctk.CTkLabel(
            left_frame, 
            text=self.t('drag_hint'),
            height=80,
            fg_color=("#3B8ED0", "#1F6AA5"),
            corner_radius=10,
            font=ctk.CTkFont(size=13)
        )
        self.drop_label.pack(pady=10, padx=10, fill="x")
        
        # 配置拖拽功能
        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind('<<Drop>>', self._drop_files)
        
        # 文件浏览按钮
        self.browse_btn = ctk.CTkButton(
            left_frame, 
            text=self.t('browse_files'), 
            command=self._add_files,
            height=35
        )
        self.browse_btn.pack(pady=5, padx=10, fill="x")
        
        # 文件列表框
        self.list_label = ctk.CTkLabel(left_frame, text=self.t('selected_files'), 
                                   font=ctk.CTkFont(size=12))
        self.list_label.pack(pady=(10, 5), padx=10, anchor="w")
        
        # 创建文件列表框架
        list_frame = ctk.CTkFrame(left_frame)
        list_frame.pack(pady=5, padx=10, fill="both", expand=True)
        
        # 文件列表文本框（带滚动条）
        self.file_listbox = ctk.CTkTextbox(list_frame, height=150, wrap="none")
        self.file_listbox.pack(fill="both", expand=True)
        
        # 列表操作按钮
        list_btn_frame = ctk.CTkFrame(left_frame, fg_color="transparent")
        list_btn_frame.pack(pady=5, padx=10, fill="x")
        
        self.remove_btn = ctk.CTkButton(
            list_btn_frame, 
            text=self.t('remove_selected'), 
            command=self._remove_selected,
            width=120,
            fg_color="#D35B58",
            hover_color="#C72C28"
        )
        self.remove_btn.pack(side="left", padx=(0, 5))
        
        self.clear_btn = ctk.CTkButton(
            list_btn_frame, 
            text=self.t('clear_list'), 
            command=self._clear_files,
            width=120,
            fg_color="#D35B58",
            hover_color="#C72C28"
        )
        self.clear_btn.pack(side="left")
        
        # --- 参数配置区 ---
        self.param_label = ctk.CTkLabel(left_frame, text=self.t('parameters'), 
                                    font=ctk.CTkFont(size=16, weight="bold"))
        self.param_label.pack(pady=(20, 10))
        
        # Identity 参数
        identity_frame = ctk.CTkFrame(left_frame, fg_color="transparent")
        identity_frame.pack(pady=5, padx=10, fill="x")
        
        self.identity_label_text = ctk.CTkLabel(identity_frame, text=self.t('identity'), 
                     font=ctk.CTkFont(size=12))
        self.identity_label_text.pack(anchor="w")
        
        identity_value_frame = ctk.CTkFrame(identity_frame, fg_color="transparent")
        identity_value_frame.pack(fill="x", pady=5)
        
        self.identity_slider = ctk.CTkSlider(
            identity_value_frame, 
            from_=0.0, 
            to=1.0, 
            number_of_steps=100,
            command=self._update_identity_label
        )
        self.identity_slider.set(0.30)
        self.identity_slider.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        self.identity_label = ctk.CTkLabel(identity_value_frame, text="0.30", 
                                            width=50, font=ctk.CTkFont(size=12))
        self.identity_label.pack(side="left")
        
        # 输出文件名
        output_frame = ctk.CTkFrame(left_frame, fg_color="transparent")
        output_frame.pack(pady=5, padx=10, fill="x")
        
        self.output_name_label = ctk.CTkLabel(output_frame, text=self.t('output_filename'), 
                     font=ctk.CTkFont(size=12))
        self.output_name_label.pack(anchor="w")
        
        self.output_name_entry = ctk.CTkEntry(output_frame, height=30)
        self.output_name_entry.insert(0, self._generate_default_filename())
        self.output_name_entry.pack(fill="x", pady=5)
        
        # 输出目录
        dir_frame = ctk.CTkFrame(left_frame, fg_color="transparent")
        dir_frame.pack(pady=5, padx=10, fill="x")
        
        self.output_dir_label = ctk.CTkLabel(dir_frame, text=self.t('output_directory'), 
                     font=ctk.CTkFont(size=12))
        self.output_dir_label.pack(anchor="w")
        
        dir_select_frame = ctk.CTkFrame(dir_frame, fg_color="transparent")
        dir_select_frame.pack(fill="x", pady=5)
        
        self.output_dir_entry = ctk.CTkEntry(dir_select_frame, height=30)
        self.output_dir_entry.insert(0, self.t('auto_directory'))
        self.output_dir_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        dir_btn = ctk.CTkButton(
            dir_select_frame, 
            text="📁", 
            command=self._select_output_dir,
            width=40
        )
        dir_btn.pack(side="left")
        
        # 高级选项（可折叠）
        self.advanced_visible = False
        self.advanced_btn = ctk.CTkButton(
            left_frame,
            text=self.t('advanced_options'),
            command=self._toggle_advanced,
            fg_color="transparent",
            hover_color=("#3B8ED0", "#1F6AA5"),
            anchor="w"
        )
        self.advanced_btn.pack(pady=(10, 5), padx=10, fill="x")
        
        # 高级选项容器
        self.advanced_frame = ctk.CTkFrame(left_frame, fg_color="transparent")
        
        self.no_align_var = ctk.BooleanVar()
        self.no_align_cb = ctk.CTkCheckBox(
            self.advanced_frame, 
            text=self.t('no_align'),
            variable=self.no_align_var
        )
        self.no_align_cb.pack(anchor="w", pady=2, padx=10)
        
        self.use_file_order_var = ctk.BooleanVar()
        self.use_file_order_cb = ctk.CTkCheckBox(
            self.advanced_frame, 
            text=self.t('use_file_order'),
            variable=self.use_file_order_var
        )
        self.use_file_order_cb.pack(anchor="w", pady=2, padx=10)
        
        self.hide_link_var = ctk.BooleanVar()
        self.hide_link_cb = ctk.CTkCheckBox(
            self.advanced_frame, 
            text=self.t('hide_link_headers'),
            variable=self.hide_link_var
        )
        self.hide_link_cb.pack(anchor="w", pady=2, padx=10)
        
        self.hide_aln_var = ctk.BooleanVar()
        self.hide_aln_cb = ctk.CTkCheckBox(
            self.advanced_frame, 
            text=self.t('hide_aln_headers'),
            variable=self.hide_aln_var
        )
        self.hide_aln_cb.pack(anchor="w", pady=2, padx=10)
        
        self.force_var = ctk.BooleanVar(value=True)  # 默认覆盖
        self.force_cb = ctk.CTkCheckBox(
            self.advanced_frame, 
            text=self.t('force_overwrite'),
            variable=self.force_var
        )
        self.force_cb.pack(anchor="w", pady=2, padx=10)
        
        # ====================================================================
        # 右侧面板：执行控制和日志显示
        # ====================================================================
        right_frame = ctk.CTkFrame(self)
        right_frame.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)
        
        # --- 执行控制区 ---
        self.control_label = ctk.CTkLabel(right_frame, text=self.t('execution_control'), 
                                      font=ctk.CTkFont(size=16, weight="bold"))
        self.control_label.pack(pady=(10, 10))
        
        self.run_btn = ctk.CTkButton(
            right_frame,
            text=self.t('start_analysis'),
            command=self._run_clinker,
            height=45,
            font=ctk.CTkFont(size=15, weight="bold"),
            fg_color="#2FA572",
            hover_color="#258B5E"
        )
        self.run_btn.pack(pady=10, padx=20, fill="x")
        
        # 进度条
        self.progress_bar = ctk.CTkProgressBar(right_frame, mode="indeterminate")
        self.progress_bar.pack(pady=5, padx=20, fill="x")
        self.progress_bar.pack_forget()  # 初始隐藏
        
        # --- 日志显示区 ---
        self.log_label = ctk.CTkLabel(right_frame, text=self.t('run_log'), 
                                  font=ctk.CTkFont(size=16, weight="bold"))
        self.log_label.pack(pady=(10, 5))
        
        # 日志文本框
        self.log_text = ctk.CTkTextbox(right_frame, wrap="word", font=ctk.CTkFont(size=11))
        self.log_text.pack(pady=5, padx=20, fill="both", expand=True)
        
        # 日志操作按钮
        log_btn_frame = ctk.CTkFrame(right_frame, fg_color="transparent")
        log_btn_frame.pack(pady=5, padx=20, fill="x")
        
        self.clear_log_btn = ctk.CTkButton(
            log_btn_frame,
            text=self.t('clear_log'),
            command=self._clear_log,
            width=120
        )
        self.clear_log_btn.pack(side="left")
        
        self.open_result_btn = ctk.CTkButton(
            log_btn_frame,
            text=self.t('open_result'),
            command=self._open_result,
            width=120,
            state="disabled"
        )
        self.open_result_btn.pack(side="right")
        
        # 初始日志信息
        self._log(self.t('welcome'))
        self._log(self.t('welcome_hint') + "\n")
    
    def _on_language_change(self, choice):
        """语言切换事件处理 / Language change event handler"""
        # 根据选择的文本确定语言代码
        if choice in [LANGUAGES['zh_CN']['chinese'], '中文']:
            self.switch_language('zh_CN')
        else:
            self.switch_language('en_US')
    
    # ========================================================================
    # 文件管理相关方法 / File management methods
    # ========================================================================
    
    def _add_files(self):
        """浏览并添加文件 / Browse and add files"""
        files = filedialog.askopenfilenames(
            title=self.t('select_genome_files'),
            filetypes=[
                ("GenBank Files", "*.gbk *.gb"),
                ("GFF3 Files", "*.gff3"),
                ("All Files", "*.*")
            ]
        )
        
        if files:
            for file in files:
                abs_path = os.path.abspath(file)
                if abs_path not in self.file_paths:
                    self.file_paths.append(abs_path)
            
            self._update_file_list()
            self._log(self.t('files_added').format(len(files)))
    
    def _drop_files(self, event):
        """处理拖拽文件事件 / Handle drag and drop files event"""
        # 解析拖拽的文件路径
        files = self._parse_drop_files(event.data)
        
        added_count = 0
        for file in files:
            # 只接受特定扩展名
            if file.lower().endswith(('.gbk', '.gb', '.gff3')):
                abs_path = os.path.abspath(file)
                if abs_path not in self.file_paths:
                    self.file_paths.append(abs_path)
                    added_count += 1
        
        if added_count > 0:
            self._update_file_list()
            self._log(self.t('files_dropped').format(added_count))
        else:
            self._log(self.t('no_files_added'))
    
    def _parse_drop_files(self, data):
        """解析拖拽数据中的文件路径 / Parse file paths from drop data"""
        # Windows 拖拽数据格式处理
        files = []
        current = ""
        in_quote = False
        
        for char in data:
            if char == '{':
                in_quote = True
                current = ""
            elif char == '}':
                in_quote = False
                if current:
                    files.append(current)
                current = ""
            elif char == ' ' and not in_quote:
                if current:
                    files.append(current)
                current = ""
            else:
                current += char
        
        if current:
            files.append(current)
        
        return files
    
    def _update_file_list(self):
        """更新文件列表显示 / Update file list display"""
        self.file_listbox.delete("1.0", "end")
        for i, path in enumerate(self.file_paths, 1):
            filename = os.path.basename(path)
            self.file_listbox.insert("end", f"{i}. {filename}\n")
    
    def _remove_selected(self):
        """删除选中的文件（简化版：删除最后一个）/ Remove selected file (last one)"""
        if self.file_paths:
            removed = self.file_paths.pop()
            self._update_file_list()
            self._log(self.t('file_removed').format(os.path.basename(removed)))
    
    def _clear_files(self):
        """清空文件列表 / Clear file list"""
        if self.file_paths:
            count = len(self.file_paths)
            self.file_paths.clear()
            self._update_file_list()
            self._log(self.t('files_cleared').format(count))
    
    # ========================================================================
    # 参数配置相关方法 / Parameter configuration methods
    # ========================================================================
    
    def _update_identity_label(self, value):
        """更新 Identity 标签显示 / Update identity label"""
        self.identity_label.configure(text=f"{float(value):.2f}")
    
    def _generate_default_filename(self):
        """生成默认输出文件名 / Generate default output filename"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        return f"clinker_result_{timestamp}.html"
    
    def _select_output_dir(self):
        """选择输出目录 / Select output directory"""
        directory = filedialog.askdirectory(title=self.t('select_output_dir'))
        if directory:
            self.output_dir_entry.delete(0, "end")
            self.output_dir_entry.insert(0, directory)
            self._log(self.t('output_dir_set').format(directory))
    
    def _toggle_advanced(self):
        """切换高级选项显示/隐藏 / Toggle advanced options"""
        if self.advanced_visible:
            self.advanced_frame.pack_forget()
            self.advanced_btn.configure(text=self.t('advanced_options'))
            self.advanced_visible = False
        else:
            self.advanced_frame.pack(pady=5, padx=10, fill="x")
            self.advanced_btn.configure(text=self.t('advanced_options_open'))
            self.advanced_visible = True
    
    # ========================================================================
    # 命令构建和执行 / Command building and execution
    # ========================================================================
    
    def _build_command(self):
        """构建 clinker 命令 / Build clinker command"""
        # 基础命令
        cmd = ["clinker"]
        
        # 添加输入文件（使用绝对路径列表，避免空格问题）
        cmd.extend(self.file_paths)
        
        # 添加 identity 参数
        identity = self.identity_slider.get()
        cmd.extend(["-i", str(identity)])
        
        # 确定输出路径
        output_name = self.output_name_entry.get().strip()
        if not output_name:
            output_name = self._generate_default_filename()
        
        output_dir = self.output_dir_entry.get().strip()
        auto_dir_text = self.t('auto_directory')
        if not output_dir or output_dir == auto_dir_text:
            if self.file_paths:
                output_dir = os.path.dirname(self.file_paths[0])
            else:
                output_dir = os.getcwd()
        
        # 确保输出文件名有 .html 扩展名
        if not output_name.lower().endswith('.html'):
            output_name += '.html'
        
        self.output_file_path = os.path.join(output_dir, output_name)
        
        # 添加 plot 参数（生成 HTML）
        cmd.extend(["-p", self.output_file_path])
        
        # 添加高级选项
        if self.no_align_var.get():
            cmd.append("-na")
        
        if self.use_file_order_var.get():
            cmd.append("-ufo")
        
        if self.hide_link_var.get():
            cmd.append("-hl")
        
        if self.hide_aln_var.get():
            cmd.append("-ha")
        
        if self.force_var.get():
            cmd.append("-f")
        
        return cmd
    
    def _run_clinker(self):
        """运行 clinker（异步执行）/ Run clinker (asynchronous)"""
        # 验证输入
        if not self.file_paths:
            messagebox.showerror(self.t('error'), self.t('no_input_files'))
            return
        
        if self.is_running:
            messagebox.showwarning(self.t('warning'), self.t('task_running'))
            return
        
        # 构建命令
        try:
            cmd = self._build_command()
        except Exception as e:
            messagebox.showerror(self.t('error'), 
                               self.t('command_build_failed').format(str(e)))
            return
        
        # 更新 UI 状态
        self.is_running = True
        self.run_btn.configure(state="disabled", text=self.t('running'))
        self.progress_bar.pack(pady=5, padx=20, fill="x")
        self.progress_bar.start()
        self.open_result_btn.configure(state="disabled")
        
        # 清空日志
        self._log("\n" + "="*60)
        self._log(self.t('start_execution'))
        self._log(self.t('command').format(' '.join(cmd)))
        self._log("="*60 + "\n")
        
        # 在新线程中执行
        thread = threading.Thread(target=self._execute_clinker, args=(cmd,), daemon=True)
        thread.start()
    
    def _execute_clinker(self, cmd):
        """在后台线程中执行 clinker / Execute clinker in background thread"""
        try:
            # Windows 平台隐藏控制台窗口的配置
            startupinfo = None
            creationflags = 0
            
            if sys.platform == 'win32':
                # 在 Windows 上隐藏控制台窗口
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = subprocess.SW_HIDE
                # 使用 CREATE_NO_WINDOW 标志（Windows）
                creationflags = 0x08000000  # CREATE_NO_WINDOW
            
            # 使用 Popen 异步执行，捕获输出
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8',
                errors='replace',
                bufsize=1,
                universal_newlines=True,
                startupinfo=startupinfo,
                creationflags=creationflags
            )
            
            # 实时读取 stdout 输出
            while True:
                output = process.stdout.readline()
                if output:
                    self._log(output.strip())
                
                # 检查进程是否结束
                if process.poll() is not None:
                    break
            
            # 读取剩余输出
            remaining_output, remaining_error = process.communicate()
            
            if remaining_output:
                self._log(remaining_output.strip())
            
            # 处理 stderr 输出
            # clinker 将 INFO 日志也输出到 stderr，需要智能判断是否为真正的错误
            if remaining_error:
                stderr_lines = remaining_error.strip()
                # 检查是否包含真正的错误关键词
                is_real_error = any(keyword in stderr_lines for keyword in [
                    'ERROR', 'Error', 'error:', 'CRITICAL', 'Critical',
                    'Traceback', 'Exception', 'FAILED', 'Failed'
                ])
                
                # 如果不是真正的错误，就作为普通日志显示
                if is_real_error or process.returncode != 0:
                    self._log(f"\n{self.t('error_info')}\n{stderr_lines}", error=True)
                else:
                    # clinker 的 INFO 日志，作为普通日志显示
                    self._log(f"\n{stderr_lines}")
            
            # 检查返回码
            if process.returncode == 0:
                self._log("\n" + "="*60)
                self._log(self.t('analysis_complete'))
                self._log(self.t('result_file').format(self.output_file_path))
                self._log("="*60)
                
                # 在主线程中更新 UI
                self.after(0, self._on_success)
            else:
                self._log("\n" + "="*60)
                self._log(self.t('analysis_failed').format(process.returncode))
                self._log("="*60)
                
                self.after(0, self._on_failure)
        
        except FileNotFoundError:
            self._log(f"\n{self.t('clinker_not_found')}", error=True)
            self._log(self.t('clinker_install_hint'), error=True)
            self.after(0, self._on_failure)
        
        except Exception as e:
            self._log(f"\n{self.t('execution_error').format(str(e))}", error=True)
            self.after(0, self._on_failure)
    
    def _on_success(self):
        """执行成功后的处理 / Post-execution success handler"""
        self.is_running = False
        self.run_btn.configure(state="normal", text=self.t('start_analysis'))
        self.progress_bar.stop()
        self.progress_bar.pack_forget()
        self.open_result_btn.configure(state="normal")
        
        # 弹窗提示
        result = messagebox.askyesno(
            self.t('success'),
            self.t('analysis_complete_dialog').format(self.output_file_path)
        )
        
        if result:
            self._open_result()
    
    def _on_failure(self):
        """执行失败后的处理 / Post-execution failure handler"""
        self.is_running = False
        self.run_btn.configure(state="normal", text=self.t('start_analysis'))
        self.progress_bar.stop()
        self.progress_bar.pack_forget()
        
        messagebox.showerror(self.t('error'), self.t('analysis_failed_dialog'))
    
    # ========================================================================
    # 日志和结果处理 / Log and result handling
    # ========================================================================
    
    def _log(self, message, error=False):
        """添加日志信息 / Add log message"""
        self.log_text.insert("end", message + "\n")
        
        # 错误信息使用红色（如果支持）
        if error:
            # CustomTkinter 的 CTkTextbox 不直接支持 tag，这里简化处理
            pass
        
        self.log_text.see("end")
    
    def _clear_log(self):
        """清空日志 / Clear log"""
        self.log_text.delete("1.0", "end")
    
    def _open_result(self):
        """打开结果 HTML 文件 / Open result HTML file"""
        if self.output_file_path and os.path.exists(self.output_file_path):
            try:
                webbrowser.open(self.output_file_path)
                self._log(self.t('result_opened').format(self.output_file_path))
            except Exception as e:
                messagebox.showerror(self.t('error'), 
                                   self.t('cannot_open_file').format(str(e)))
        else:
            messagebox.showwarning(self.t('warning'), self.t('file_not_exists'))


# ============================================================================
# 主程序入口 / Main program entry point
# ============================================================================

def main():
    """主函数 / Main function"""
    app = ClinkerGUI()
    app.mainloop()


if __name__ == "__main__":
    main()


# ============================================================================
# PyInstaller 打包说明 / PyInstaller Packaging Instructions
# ============================================================================
"""
将此程序打包成独立的 .exe 文件 / Package this program as a standalone .exe file

1. 安装 PyInstaller / Install PyInstaller:
   pip install pyinstaller

2. 打包命令（目录模式，推荐）/ Package command (directory mode, recommended):
   pyinstaller --windowed --name "ClinkerGUI" --hidden-import tkinterdnd2 --hidden-import tkinterdnd2.tkdnd clinker_gui.py

3. 打包后 / After packaging:
   - 可执行文件位于 dist/ClinkerGUI/ 目录中
   - Executable file is in dist/ClinkerGUI/ directory
   - 将整个文件夹分发给用户 / Distribute the entire folder to users
   - 用户需要确保系统中已安装 clinker / Users need clinker installed on their system

4. 常见问题 / Common issues:
   - 如遇到 tkinterdnd2 相关错误，使用目录模式打包
   - If encounter tkinterdnd2 errors, use directory mode
   - Windows Defender 可能误报，需添加信任
   - Windows Defender may flag it, add to trusted list
"""
