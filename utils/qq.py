"""
QQ 使用通道添加QQ好友2933206697
http://gm.zhoudedi.top:300/
"""
import requests


def qq_push(key, qq_num, msg, type, send_type="send_msg"):
    """
    :param key: QQ的key，默认xiaohzou 使用通道添加QQ好友：2933206697
    :param qq_num: qq号或qq群组号，要与 type 对应
    :param msg: 发送消息
    :param type: 发送模式，"private"为发送给个人，"group"为发送给群组
    :return:
    """
    post_data = {
        "message_type": type,
        "user_id": qq_num,
        'group_id': qq_num,
        "message": msg,
    }
    try:
        # http://gm.zhoudedi.top:300/send_msg?group_id=**QQ群**&user_id=**QQ**&message=**发送内容**
        res = requests.post(f"http://gm.zhoudedi.top:300/{send_type}", data=post_data).json()
        """
        {"data":{"message_id":-1388401960},"retcode":0,"status":"ok"}
        {"data":null,"msg":"EMPTY_MSG_ERROR","retcode":100,"status":"failed","wording":"消息为空"}
        """
        if not res["retcode"]:
            return {"status": 1, "msg": "QQ推送服务成功"}
        else:
            return {"status": 0, "errmsg": f"QQ推送服务失败，{res['wording']}"}
    except Exception as e:
        return {"status": 0, "errmsg": f"QQ推送服务失败，{e}"}