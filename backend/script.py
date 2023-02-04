from time import sleep
from revChatGPT.ChatGPT import Chatbot
# from pocketsphinx import LiveSpeech



chatbot = Chatbot({
  "session_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..1q9xL9ymfDM_GYF3.gigaRYIz1A5tQvUwvs2FnCvUDQZ5Zcg6rsFCwRbaJ0kczY99zesFcJApEYnjifZINRInTnvOrTko8UnTELkAiVaqtAAylCQ2rYVlUQCaL6nx62yeRboR0jqzCC3dZzUj7LlkJegP2TNtRHHbT3VwfC_KYJR3PwAsvmmPkWJTkqgU8yJ36WPfR1slLaB38oKz72ojIt52KL0a88j0aLGRgvKAp9HiOvuCu1wgCyXj80fulV1lEx-T4HqDutkSaXCqS5RHX30So-gTAbcD7aRtx1jIGNJk8LR1S5pXkGX98_4at4Ub2zPmM2H7Pbfz5qE0t6NU2C8Izxjcu1qxdYqkMgeRCVBFnjeyC6fQTP7Txb4YYBx6_hm0468Z536LrVZzN3ar3M2zRuadnFf-Zzlfm0j2ZLzdVZVSE8vOmwqfTcNm0uhajL8hGEazR8sPI8ZJBcCHN9loDBQfR17TQpesXAsF2hW5L_CVMmq6wAqDFfN1fZ4iNAAer-AVharxrc5T1TWx_WTlMYA-QDjcYpX5pcI_i1FbKBd1GzETxByRzUlkjJsLwIT1iR4moD1wHEtl2ar7hr91QQI0tsrPoFkrFiOZQaw0gMJT1Xo2mN1wqSdjYWW-UBJDG7YcVQJgK3Gf7hoHg-5UnOAFmnsd276qUtLndtFDSS06hY_OnSXKFw3U-3PKv45hNsHHuAkLC2npCUE_aYRuZ9WGHXpbsHYMSwoxt_JLUQTkCL__bc1HreuLN30vDfsLRDRJEhShtOB5XqaGrkP-bZCUsTgvWjO41j2CFjISHXVas5SnFrGEFa8Pm1G_VJaQlTNvAp-GvWGIb3AtRQLWHHZd5op1u80tFMgrxpAJvXQfBM5sEHTaEPlrDlaGycOB11v1eDdp7tUdxFNwnoHHB1XkXVa_5qm3DRh78ICRyF3k4kd9K1ibZ0SU-0Lwu7XzbhEFCVIOdJ4UnKKBRbUdSV8vfLgMTSwZhlQQK67speVq405LS5Pcafr1_iYZYvWeL2p7hwjkRMTAMC_4dgEQovxr40PDWy2_UTkXGiTBUZGLvQ28yui1UtQmhdMwh4fc3zkzWq1kxFWbQyn9skfZ5_BjKiwtmSqEq5CQb6xJWlbjZcBjPWrNlRpzly1dkCZj8-ycRBYo4hkOOK3EMQknyQ0rRmLpdHCWgzSLx8zI5e-WUy6Kq7A60Iy-hQJhALmEdL_SymX62b3WweJ2Cmp0rq-WmJ75I1ZT_iTQ9Ke9E5qEL7d9mWT11TB2JhDtsGZERE0oSlyLtOIUSr33PMelEuWH7OGqfsUsQgjCawhRZEkUkMPm37fU8Qd5RSYQQtFjEbkYK72fh3BM5-i_omU8MMcz04BlOATjnKRiCIBYsPMFT5wgwc9amHiFL6e0qMUp7IX5B5KHwMVo70FRmna6WvX9gohUcrpRhlPus1kUUumBKcvaSdENarywOuLBAB7xeHKrXeb4TtF1G7VsOX4eiP_DflvUvDu2nTA2wqdA8tV4dnCwnrxKzESY7JiiNKPwyK21fxxrbzcTY_My3_vpUlBBcLEHhqgXVxXbtjhtp1J3HRLyjZsBu9OMHvteCAQOh2bjZS9uoZwdxufXgKQCWOtKIrOVJ7-aoJf_yYai0v424H5c6iS16scbXS1h1-bIq-5IAB4cYr-dPwHjrs5qUBxE7uKKPKZIhhQrXQ_FG1QvCWLXRFtfdKQmCcbHyTfr9zFaytrnZDleXgQw8rxoSkrNwTt_sHW38lGrrkZw8zpgZM3IggylQDIEUyeLPhZCQ6otYZBL7g5LdB0U5m0KNk2xDlCeDox7ZueBdVFHxLWYeJkyuZ0p7QFlF2C1auLog3BT0eXfEIPTo-mrMaxLc4hYKs2uA36S11Bvbz8IrC2sarGcjHESx6OooUwipoq1IQEjtH9r4HPu3KY_0oSVzl_YN_xfd7yA2vgEhDi8-OvK88WrDCmspsOzKIjeOpOK_ygJ8_L0QiurtuclXS8mOz6QkWuncFMR8331JenPQY3AQPaMROu6cpECGrzAV9g_kuCBOCP1aH147QqRzgCyNHPsQ0LSnF5GHR3GvesBTIM52GllOxsdokYIlePUgXUH3540L1Kqm13lVotlptC7VocUlZrdfVwMaZDPASpZgOFKWtIKK_4l48fBGNBV5tt3BvP8AEBaQSi9FxonbBykiMBS_qz1LLgMTwV_4yfvGkJ2t_nlikReo9OcHBjAoL0b2y29GzRUc6Lo3as52JR3_xEL_AE3oBVTE_f4l_dzdIOlMnQIT-KIN4hkjlgrFVdLERAGfnkA2Rctapc9obawbxjLHWPRHfqJCD3_lYFtcYYd2nn0R-wE2LvfZ1CDLRDCoO0RWqe0lG5jQDKKF9fUMUJzefH-mOmmQ0K4ZAomp105gsyvfuUa9CZXAEGlCpZ0sh8c-mGURxzD4DdEbRQ7w8ZLqGndFjPKyk6I-jUe2_2owS18N81pW1Zkl49m16TDCZtEOMoqFJDVH1F2uIpjJDDS-HhNBCZO_QG-B_hG.qkuCG_Nem9IiiVZwLHvBaQ"
}, conversation_id=None, parent_id=None) # You can start a custom conversation

talk_time = 1 #seconds
# first
print("listening...")
# sleep(talk_time)
while True:
    # prompt = input("write:")
    prompt = "hello"
    print(prompt)
    print("processing..")
    response = chatbot.ask(str(prompt), conversation_id=None, parent_id=None)
# prompt = "what is life"
    print(response)
    print("listening...")
    # sleep(talk_time)
    sleep(20)



