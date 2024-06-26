# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.1.0a2 on Mon Apr 29 10:08:57 2024
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((843, 850))
        self.SetTitle("OSC Parameter Editor ")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_1.Add((20, 20), 0, wx.EXPAND, 0)

        grid_sizer_1 = wx.FlexGridSizer(1, 13, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.ALIGN_RIGHT, 0)

        label_6 = wx.StaticText(self, wx.ID_ANY, "XOSC File :  ")
        grid_sizer_1.Add(label_6, 0, 0, 0)

        self.text_ctrl_6 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_6.SetMinSize((600, 20))
        grid_sizer_1.Add(self.text_ctrl_6, 0, 0, 0)

        grid_sizer_1.Add((20, 20), 0, wx.EXPAND, 0)

        self.button_2 = wx.Button(self, wx.ID_ANY, u"…")
        self.button_2.SetMinSize((40, 20))
        grid_sizer_1.Add(self.button_2, 0, wx.ALIGN_RIGHT, 0)

        grid_sizer_1.Add((20, 20), 0, 0, 0)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_3, 1, 0, 0)

        sizer_3.Add((20, 20), 0, wx.EXPAND, 0)

        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_3.Add(sizer_9, 1, wx.EXPAND, 0)

        sizer_9.Add((400, 20), 0, 0, 0)

        self.TreePanel = wx.TreeCtrl(self, wx.ID_ANY, style=wx.FULL_REPAINT_ON_RESIZE)
        self.TreePanel.SetMinSize((400, 719))
        sizer_9.Add(self.TreePanel, 0, wx.EXPAND | wx.TOP, 0)

        sizer_9.Add((20, 5), 0, wx.EXPAND, 0)

        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_3.Add(sizer_6, 1, 0, 0)

        sizer_6.Add((20, 20), 0, wx.EXPAND, 0)

        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6.Add(sizer_11, 1, wx.EXPAND, 0)

        sizer_11.Add((10, 20), 0, 0, 0)

        label_4 = wx.StaticText(self, wx.ID_ANY, "Value         :")
        label_4.SetMinSize((70, 20))
        sizer_11.Add(label_4, 0, wx.EXPAND, 0)

        sizer_11.Add((20, 20), 0, 0, 0)

        self.text_ctrl_4 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        self.text_ctrl_4.SetMinSize((260, 20))
        sizer_11.Add(self.text_ctrl_4, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        sizer_11.Add((10, 20), 0, 0, 0)

        sizer_6.Add((20, 20), 0, wx.EXPAND, 0)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6.Add(sizer_4, 0, 0, 0)

        sizer_4.Add((10, 20), 0, 0, 0)

        label_1 = wx.StaticText(self, wx.ID_ANY, "Parameter :")
        label_1.SetMinSize((70, 20))
        sizer_4.Add(label_1, 0, wx.EXPAND, 0)

        sizer_4.Add((20, 20), 0, 0, 0)

        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_1.SetMinSize((260, 20))
        self.text_ctrl_1.SetToolTip("$parameter")
        sizer_4.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        sizer_4.Add((10, 20), 0, 0, 0)

        sizer_6.Add((20, 20), 0, wx.EXPAND, 0)

        static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        sizer_6.Add(static_line_1, 0, wx.ALL | wx.EXPAND, 2)

        sizer_6.Add((20, 20), 0, wx.EXPAND, 0)

        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)

        sizer_7.Add((10, 20), 0, 0, 0)

        label_2 = wx.StaticText(self, wx.ID_ANY, "lowerLimit  :")
        label_2.SetMinSize((70, 20))
        sizer_7.Add(label_2, 0, 0, 0)

        sizer_7.Add((20, 20), 0, 0, 0)

        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_2.SetMinSize((260, 20))
        sizer_7.Add(self.text_ctrl_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        sizer_7.Add((10, 20), 0, 0, 0)

        sizer_6.Add((20, 20), 0, wx.EXPAND, 0)

        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6.Add(sizer_8, 1, wx.EXPAND, 0)

        sizer_8.Add((10, 20), 0, 0, 0)

        label_3 = wx.StaticText(self, wx.ID_ANY, "upperLimit  :")
        label_3.SetMinSize((70, 20))
        sizer_8.Add(label_3, 0, 0, 0)

        sizer_8.Add((20, 20), 0, 0, 0)

        self.text_ctrl_3 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_3.SetMinSize((260, 20))
        sizer_8.Add(self.text_ctrl_3, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        sizer_8.Add((10, 20), 0, 0, 0)

        sizer_6.Add((20, 20), 0, wx.EXPAND, 0)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6.Add(sizer_5, 1, wx.EXPAND, 0)

        sizer_5.Add((10, 20), 0, 0, 0)

        label_5 = wx.StaticText(self, wx.ID_ANY, "stepWidth :")
        sizer_5.Add(label_5, 0, 0, 0)

        sizer_5.Add((20, 20), 0, 0, 0)

        self.text_ctrl_5 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_5.SetMinSize((260, 20))
        sizer_5.Add(self.text_ctrl_5, 0, wx.EXPAND, 0)

        sizer_5.Add((10, 20), 0, 0, 0)

        sizer_6.Add((20, 50), 0, wx.EXPAND, 0)

        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6.Add(sizer_10, 1, wx.ALIGN_RIGHT, 0)

        self.button_3 = wx.Button(self, wx.ID_ANY, "button_3")
        sizer_10.Add(self.button_3, 0, 0, 0)

        sizer_10.Add((20, 20), 0, wx.EXPAND, 0)

        self.button_1 = wx.Button(self, wx.ID_ANY, "Apply")
        sizer_10.Add(self.button_1, 0, wx.RIGHT, 0)

        sizer_10.Add((20, 20), 0, 0, 0)

        sizer_2 = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self.button_OK = wx.Button(self, wx.ID_OK, "")
        self.button_OK.SetDefault()
        sizer_2.AddButton(self.button_OK)

        self.button_CANCEL = wx.Button(self, wx.ID_CANCEL, "")
        sizer_2.AddButton(self.button_CANCEL)

        sizer_2.Realize()

        grid_sizer_1.AddGrowableRow(0)

        self.SetSizer(sizer_1)

        self.SetAffirmativeId(self.button_OK.GetId())
        self.SetEscapeId(self.button_CANCEL.GetId())

        self.Layout()

        self.button_2.Bind(wx.EVT_BUTTON, self.OnSelectFile)
        self.TreePanel.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnTreeSelChanged)
        self.button_1.Bind(wx.EVT_BUTTON, self.OnParamsApply)
        self.button_OK.Bind(wx.EVT_BUTTON, self.OnOk)
        self.button_CANCEL.Bind(wx.EVT_BUTTON, self.OnCancel)
        # end wxGlade

    def OnSelectFile(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'OnSelectFile' not implemented!")
        event.Skip()

    def OnTreeSelChanged(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'OnTreeSelChanged' not implemented!")
        event.Skip()

    def OnParamsApply(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'OnParamsApply' not implemented!")
        event.Skip()

    def OnOk(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'OnOk' not implemented!")
        event.Skip()

    def OnCancel(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'OnCancel' not implemented!")
        event.Skip()

# end of class MyDialog
