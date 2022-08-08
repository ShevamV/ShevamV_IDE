import tkinter as tk

from .. import SidebarView

# from ....placeholders.git import GitPlaceHolder
# from .container import GitTreeContainer
# from .toolbar import GitTreeToolbar


class SourceControl(SidebarView):
    def __init__(self, master, *args, **kwargs):
        self.__buttons__ = [('ellipsis', lambda e: None)]
        super().__init__(self, master, *args, **kwargs)
        
        self.master = master
        self.base = master.base

        tk.Label(self, text="Source control").pack()

    #     self.name = "Source Control"
    #     self.icon = "\uea68"
    #     self.tree_active = False
    #     self.config(bg="#f3f3f3")

    #     self.grid_rowconfigure(2, weight=1)
    #     self.grid_columnconfigure(0, weight=1)

    #     self.placeholder = GitPlaceHolder(self)
    #     self.placeholder.grid(row=1, column=0, sticky=tk.NSEW, padx=25, pady=10)

    #     #self.toolbar = GitTreeToolbar(self)
    #     self.toolbar.grid(row=0, column=0, sticky=tk.EW, pady=10)
    #     self.toolbar.disable_tools()

    #     self.tree = GitTreeContainer(self)
    #     self.update_panes()
    
    # def create_root(self):
    #     self.tree.open_repo_dir()
    
    # def disable_tree(self):
    #     if self.tree_active:
    #         self.toolbar.disable_tools()
    #         self.tree.grid_remove()
    #         self.placeholder.grid()
    #         self.tree_active = False
    
    # def enable_tree(self):
    #     if not self.tree_active:
    #         self.toolbar.enable_tools()
    #         self.placeholder.grid_remove()
    #         self.tree.grid(row=2, column=0, sticky=tk.NSEW)
    #         self.tree_active = True
    
    # def update_panes(self):
    #     if self.base.active_dir is not None:
    #         self.enable_tree()
    #     else:
    #         self.disable_tree()
