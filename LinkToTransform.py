import nuke

def Link():
	#Create and link a Transform node to the selected tracker


	t = nuke.selectedNode().knob("name").value()
	n = nuke.nodes.Transform()
	if nuke.selectedNode().Class() == "Tracker4":
		n["translate"].setSingleValue(False)
		n["translate"].setExpression("%s.translate.x" % t, 0)
		n["translate"].setExpression("%s.translate.y" % t, 1)
		n["rotate"].setExpression("%s.rotate" % t)
		n["scale"].setExpression("%s.scale" % t)
		n["center"].setSingleValue(False)
		n["center"].setExpression("%s.center.x" % t, 0)
		n["center"].setExpression("%s.center.y" % t, 1)

		n["label"].setValue("MATCHMOVE")
