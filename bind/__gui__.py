import wx
import os,sys
import wx.gizmos
import wx.lib.mixins.inspection as wit
import wx.dataview
import json


sys.path.append('pyosc-0.0.1-py3.11-macosx-10.9-universal2.egg')
sys.path.append('.')

import pyxosc
from pyxosc import xosc

class XoSC(object):
    def __init__(self,osc):
        self.osc = osc 

    def load(self,fname):
        self.osc.load(fname)
        self.osc.parse()
        self.osc.filename = os.path.basename(fname)
        self.osc.params = {}
        self.osc.param_objs = {}

    def getChildren(self,osc_o):
        ch = {}
        if (osc_o) in [ None ,[] ] : return ch
        if str(type(osc_o)).find("e_")!=-1 : return ch
        for o in dir(osc_o):
            if (str(o).find('__')!=-1):continue
            val = getattr(osc_o,o)
            if type(val) in [type(1),type(0.0),type('')]: continue
            ch[o] = val
        return ch

    def get_value(self,osc_o):
        if (str(type(osc_o)).find('pyxosc.UnsignedInt')!=-1):
            return osc_o.m_unsignedInt
        elif (str(type(osc_o)).find('pyxosc.Int')!=-1):
            return osc_o.m_int
        elif (str(type(osc_o)).find('pyxosc.String')!=-1):
            return osc_o.m_string
        elif (str(type(osc_o)).find('pyxosc.Double')!=-1):
            return osc_o.m_double
        elif (str(type(osc_o)).find('pyxosc.Boolean')!=-1):
            return osc_o.m_boolean
        elif (str(type(osc_o)).find('pyxosc.UnsignedShort')!=-1):
            return osc_o.m_unsignedShort
        return ''
    
    def get_e_parameterType(self,osc_o):
        if (str(type(osc_o)).find('pyxosc.UnsignedInt')!=-1):
            return pyxosc.e_ParameterType.unsignedInt
        elif (str(type(osc_o)).find('pyxosc.Int')!=-1):
            return pyxosc.e_ParameterType.integer
        elif (str(type(osc_o)).find('pyxosc.String')!=-1):
            return pyxosc.e_ParameterType.string
        elif (str(type(osc_o)).find('pyxosc.Double')!=-1):
            return pyxosc.e_ParameterType.double
        elif (str(type(osc_o)).find('pyxosc.Boolean')!=-1):
            return pyxosc.e_ParameterType.boolean
        elif (str(type(osc_o)).find('pyxosc.UnsignedShort')!=-1):
            return pyxosc.e_ParameterType.unsignedShort
        return pyxosc.e_ParameterType.double

    def gen_param_decls(self):
        if len(self.osc.params)== 0: return
        ParameterDecls = self.osc.OpenSCENARIO.OpenScenarioCategory.ScenarioDefinition.ParameterDeclarations
        decl_list = []
        for param,defns in self.osc.params.items():
            parameter_decl = pyxosc.ParameterDeclaration()
            p_n = pyxosc.String(); p_n.m_string = param
            p_v = pyxosc.String(); p_v.m_string = defns['value']
            p_t = pyxosc.ParameterType(); p_t.parameterType = self.get_e_parameterType(self.osc.param_objs[param])
            parameter_decl.name = p_n; parameter_decl.value = p_v ; parameter_decl.parameterType = p_t
            decl_list.append(parameter_decl)
        ParameterDecls.ParameterDeclaration = decl_list
    
    def gen_param_variations_f(self,f_out,params_dict):
        if len(params_dict) == 0: return
        with open(f_out,'w') as f:
            json.dump(params_dict,f)
        return


class TreeCtrl(wx.Panel,XoSC):
    def __init__(self, parent, osc):
        XoSC.__dict__['__init__'](self,osc)
        self.osc = osc
        wx.Panel.__init__(self, parent)
        # initialize Tree Control
        il = wx.ImageList(16, 16)
        il.Add(wx.ArtProvider.GetBitmap(wx.ART_WARNING, wx.ART_OTHER, (16, 16)))
        self.tree = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE | wx.BORDER_STATIC | wx.TR_LINES_AT_ROOT | wx.TR_NO_BUTTONS | wx.TR_ROW_LINES | wx.TR_SINGLE)
        self.tree.Create
        self.tree.AssignImageList(il)
        self.root = self.tree.AddRoot("")
        self.tree.SetClientSize((400,650))

        h_sizer = wx.BoxSizer(wx.HORIZONTAL) 
        h_sizer.Add(self.tree, 1, wx.EXPAND) 
        v_sizer = wx.BoxSizer(wx.VERTICAL) 
        # v_sizer.Add(self.tree, 0, wx.EXPAND) 
        v_sizer.Add(h_sizer, 1, wx.EXPAND) 
        self.SetSizer(v_sizer) 

        # self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnTreeSelect)
        self.tree.EnsureVisible(self.root)
    

    def OnChild(self,ch_o,itm):
        self.tree.InvalidateBestSize()
        for k,v in self.getChildren(ch_o).items():
            if v in [None]: continue
            if k in ['m_expression']: self.tree.SetItemImage(itm,0); continue
            if k in ['m_parameter']: 
                if self.tree.GetItemImage(itm) != 0: 
                    self.tree.SetItemImage(itm,0)
                continue
            itm_c = self.tree.AppendItem(itm, k)
            self.tree.SetItemText(itm_c, "%s   (%s) " % (k,str(v)))
            # self.tree.SetItemText(itm_c, str(v))
            self.tree.SetItemData(itm_c,v)
            if (self.get_value(v) not in [None,'']):
                self.tree.SetItemText(itm_c, "%s  [ %s ]   (%s) " % (k,self.get_value(v),str(v)))
            #     self.tree.SetItemText(itm_c, str(self.get_value(v)))
                self.tree.EnsureVisible(itm_c)
            if (k in ['m_expression']):
                self.tree.SetItemImage(itm,0)
                # self.tree.SetItemImage(itm_c,2)
            # if (k in ['m_parameter']):
            #     self.tree.SetItemImage(itm_c,1)
            if ((type(v) == type([])) and (len(v) > 0)):
                for idx,c in enumerate(v):
                    itm_g = self.tree.AppendItem(itm_c,'%s_%d'%(k,idx))
                    self.OnChild(c,itm_g)
            else: 
                self.OnChild(v,itm_c)

    def OnInit(self):
        fname = self.tree.AppendItem(self.root,self.osc.filename)
        self.tree.Expand(fname)
        self.OnChild(self.osc.OpenSCENARIO,fname)
        self.tree.SetClientSize(self.tree.GetBestSize())
        self.tree.EnsureVisible(self.root)

'''
class TreeListPanel(wx.Panel,XoSC):
    def __init__(self, parent, osc):
        XoSC.__dict__['__init__'](self,osc)
        self.osc = osc
        wx.Panel.__init__(self, parent)
        # initialize Tree Control
        il = wx.ImageList(16, 16)
        il.Add(wx.ArtProvider.GetBitmap(wx.ART_WARNING, wx.ART_OTHER, (16, 16)))
        il.Add(wx.ArtProvider.GetBitmap(wx.ART_CROSS_MARK, wx.ART_OTHER, (16, 16)))
        il.Add(wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_OTHER, (16, 16)))
        self.tree = wx.dataview.TreeListCtrl(self, wx.ID_ANY, wx.DefaultPosition, (800,1600), style=wx.DEFAULT_FRAME_STYLE)
        self.tree.Create
        self.tree.AssignImageList(il)
        # create Tree Control using Create() method
        self.tree.AppendColumn("Entity", 500)
        self.tree.AppendColumn("Item", 200)
        self.tree.AppendColumn("Value", 100)
        self.root = self.tree.GetRootItem()
        # # Expand whole tree
        self.OnInit()
        self.tree.Expand(self.root)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        self.SetSizer(sizer)

    def OnChild(self,ch_o,itm):
        for k,v in self.getChildren(ch_o).items():
            if v in [None]: continue
            itm_c = self.tree.AppendItem(itm, k)
            self.tree.SetItemText(itm_c, 0, k)
            self.tree.SetItemText(itm_c, 2, str(v))
            self.tree.SetItemData(itm_c,v)
            if (self.get_value(v) not in [None,'']):
                self.tree.SetItemText(itm_c, 1, str(self.get_value(v)))
                self.tree.Expand(itm_c)
            if (k in ['m_expression']):
                self.tree.SetItemImage(itm,0)
                self.tree.SetItemImage(itm_c,2)
            if (k in ['m_parameter']):
                self.tree.SetItemImage(itm_c,1)
            if ((type(v) == type([])) and (len(v) > 0)):
                for idx,c in enumerate(v):
                    itm_g = self.tree.AppendItem(itm_c,'%s_%d'%(k,idx))
                    self.OnChild(c,itm_g)
            else: 
                self.OnChild(v,itm_c)

    def OnInit(self):
        fname = self.tree.AppendItem(self.root,self.osc.filename)
        self.tree.Expand(fname)
        self.OnChild(self.osc.OpenSCENARIO,fname)
'''


class Dialog(wx.Dialog,XoSC):
    def __init__(self,osc):
        XoSC.__dict__['__init__'](self,osc)
        self.name = "XOSC Parameter Editor" #os.path.splitext(os.path.basename(__file__))[0]
        wx.Dialog.__init__(self, None, title=self.name, size=(800,850))

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

        self.TreePanel = TreeCtrl(self, self.osc)
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
    
    def OnTreeSelChanged(self, evt):  # wxGlade: MyDialog.<event_handler>
        obj = self.TreePanel.tree.GetItemData(evt.GetItem())
        if hasattr(obj,"m_parameter"):
            value = self.get_value(obj) 
            self.text_ctrl_4.SetValue(f"{value}")
            self.text_ctrl_1.SetValue(f"{obj.m_parameter.get()}")
        else:
            self.text_ctrl_4.SetValue(f"{obj}")
            self.text_ctrl_1.SetValue(f"")
        evt.Skip()
    
    def OnSelectFile(self,evt):
        dlg_f = wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",
            wildcard="*.xosc|xosc",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
            )
        if dlg_f.ShowModal() == wx.ID_OK:
            xosc_file = dlg_f.GetPath()
            self.text_ctrl_6.SetValue(xosc_file)
            if (os.path.isfile(xosc_file)):
                self.load(xosc_file)
                self.TreePanel.root.name = xosc_file
                self.TreePanel.OnInit()
        dlg_f.Destroy()

    def OnParamsApply(self, evt):  
        obj = self.TreePanel.tree.GetItemData(self.TreePanel.tree.GetSelection())
        if obj in [None]: evt.Skip() ; return
        if (self.text_ctrl_1.GetValue() not in [None,'']):
            v = self.text_ctrl_1.GetValue()
            if (not v.startswith('$')) : v = f'${v}'
            obj.m_parameter.set(v)
            self.osc.params[v] = {"upperLimit": self.text_ctrl_3.GetValue() , "lowerLimit": self.text_ctrl_2.GetValue() , "stepWidth" : self.text_ctrl_5.GetValue() , "value": self.text_ctrl_4.GetValue()}
            self.osc.param_objs[v] = obj
        evt.Skip()

    def OnOk(self, evt):  
        params_fout = self.osc.filename.replace(".xosc","_VARIATIONS.xosc")
        self.gen_param_decls()
        self.gen_param_variations_f(params_fout,self.osc.params)
        fout = self.osc.filename.replace(".xosc","_TEMPLATE.xosc")
        self.osc.save(fout)
        evt.Skip()
        self.Destroy()

    def OnCancel(self, evt):  
        evt.Skip()
        self.Destroy()


# class App(wx.App,wit.InspectionMixin):
class App(wx.App):
    def __init__(self):
        wx.App.__init__(self)

    def OnInit(self):
        self.osc = xosc()
        self.panel = Dialog(self.osc)
        self.panel.Show()
        return True
        

def main():
    app = App()
    app.MainLoop()
 
if __name__ == '__main__':
    main()