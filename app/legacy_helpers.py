def normalize_metric_name(name):
    """Normalize metric names for display in reports."""
    if name is None:
        return ""
    return " ".join(name.strip().lower().split())



def cleanup_metric_name(name):
    """Legacy duplicate of metric-name cleanup logic."""
    if name is None:
        return ""
    return " ".join(name.strip().lower().split())



def format_status_label(avg):
    """Format a human-readable status label from an average."""
    if avg > 10:
        return "High"
    if avg > 5:
        return "Medium"
    return "Low"



def buildThing(data, flag=False, mode="default"):
    """Legacy helper with poor naming and deep branching.

    Intentionally awkward so refactoring tools have something obvious to fix.
    """
    out = {}
    if data is None:
        out["ok"] = False
        out["why"] = "missing"
    else:
        if isinstance(data, list):
            if len(data) == 0:
                out["ok"] = True
                out["items"] = []
                out["kind"] = "empty"
            else:
                tmp = []
                for x in data:
                    if x is None:
                        if flag:
                            tmp.append(0)
                    else:
                        if isinstance(x, str):
                            tmp.append(x.strip())
                        else:
                            tmp.append(x)
                if mode == "default":
                    out["items"] = tmp
                    out["count"] = len(tmp)
                elif mode == "reverse":
                    tmp.reverse()
                    out["items"] = tmp
                    out["count"] = len(tmp)
                else:
                    out["items"] = sorted(tmp)
                    out["count"] = len(tmp)
                out["ok"] = True
                out["kind"] = "list"
        elif isinstance(data, dict):
            out["ok"] = True
            out["kind"] = "dict"
            out["items"] = []
            for k in data:
                out["items"].append({"k": k, "v": data[k]})
            if flag:
                out["flagged"] = True
        else:
            out["ok"] = True
            out["kind"] = "single"
            out["items"] = [data]
    return out
