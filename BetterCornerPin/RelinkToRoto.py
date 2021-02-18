n = nuke.thisNode()
t = nuke.thisNode().knob("name").value()
x = nuke.thisNode().knob("curves")
root = x.rootLayer
v = root[0].name

with nuke.thisNode():
    nuke.selectedNode().knob('knobChanged').setValue(None)

n['from1'].setValue(0)
n['from2'].setValue(0)
n['from3'].setValue(0)
n['from4'].setValue(0)

n['from1'].setSingleValue(False)
n['from1'].setExpression("%s.CornerPinFrom.curves.%s.curve_points.3.main.x" % (t, v), 0)
n['from1'].setExpression("%s.CornerPinFrom.curves.%s.curve_points.3.main.y" % (t, v), 1)

n['from2'].setSingleValue(False)
n['from2'].setExpression("%s.CornerPinFrom.curves.%s.curve_points.2.main.x" % (t, v), 0)
n['from2'].setExpression("%s.CornerPinFrom.curves.%s.curve_points.3.main.y" % (t, v), 1)

n['from3'].setSingleValue(False)
n['from3'].setExpression("%s.CornerPinFrom.curves.%s.curve_points.1.main.x" % (t, v), 0)
n['from3'].setExpression("%s.CornerPinFrom.curves.%s.curve_points.1.main.y" % (t, v), 1)

n['from4'].setSingleValue(False)
n['from4'].setExpression("%s.CornerPinFrom.curves.%s.curve_points.3.main.x" % (t, v), 0)
n['from4'].setExpression("%s.CornerPinFrom.curves.%s.curve_points.1.main.y" % (t, v), 1)

with nuke.selectedNode():
    nuke.selectedNode().knob('knobChanged').setValue('n = nuke.thisNode()\nk = nuke.thisKnob()\np = nuke.thisKnob()\nf = nuke.thisKnob()\ng = nuke.thisKnob()\nif k.name() == "from4" and k.value() > 0:\n n["from4"].clearAnimated(),n["from2"].clearAnimated(),n["from3"].clearAnimated(),n["from1"].clearAnimated()\nif p.name() == "from2" and p.value() > 0:\n n["from4"].clearAnimated(),n["from2"].clearAnimated(),n["from3"].clearAnimated(),n["from1"].clearAnimated()\nif f.name() == "from3" and f.value() > 0:\n n["from4"].clearAnimated(),n["from2"].clearAnimated(),n["from3"].clearAnimated(),n["from1"].clearAnimated()\nif g.name() == "from1" and g.value() > 0:\n n["from4"].clearAnimated(),n["from2"].clearAnimated(),n["from3"].clearAnimated(),n["from1"].clearAnimated()')
