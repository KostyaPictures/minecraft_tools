#in which categories to search in lang file.
inp=["container.repair", "addServer.add"]
#what symbol should be placed at the end of the string
unique_symb="§f\\ueff8"
#after how many symbols 'unique_symb' should be pasted. Will create spaces.
#For ex.:
#was: "Golden apple"
#will be (if offset=16 and unique_symb='@'): "Golden apple    @"
offset=25

#assets file in .minecraft
assets="C:/Users/Kosty/AppData/Roaming/.minecraft/assets"
#index file in minecraft assets
indexes=assets+"/indexes/17.json"
#folder to output langs
output="output"

#blacklist and whitelist for languages. If there is at least 1 in either of them, program mode will be switched to blacklist/whitelist
langs_whitelist=[]
langs_blacklist=[]

############
### CODE ###
############
langs=[
    "af_za",
    "ar_sa",
    "ast_es",
    "az_az",
    "ba_ru",
    "bar",
    "be_by",
    "be_latn",
    "bg_bg",
    "br_fr",
    "brb",
    "bs_ba",
    "ca_es",
    "cs_cz",
    "cy_gb",
    "da_dk",
    "de_at",
    "de_ch",
    "de_de",
    "el_gr",
    "en_au",
    "en_ca",
    "en_gb",
    "en_nz",
    "en_pt",
    "en_ud",
    "enp",
    "enws",
    "eo_uy",
    "es_ar",
    "es_cl",
    "es_ec",
    "es_es",
    "es_mx",
    "es_uy",
    "es_ve",
    "esan",
    "et_ee",
    "eu_es",
    "fa_ir",
    "fi_fi",
    "fil_ph",
    "fo_fo",
    "fr_ca",
    "fr_fr",
    "fra_de",
    "fur_it",
    "fy_nl",
    "ga_ie",
    "gd_gb",
    "gl_es",
    "hal_ua",
    "haw_us",
    "he_il",
    "hi_in",
    "hn_no",
    "hr_hr",
    "hu_hu",
    "hy_am",
    "id_id",
    "ig_ng",
    "io_en",
    "is_is",
    "isv",
    "it_it",
    "ja_jp",
    "jbo_en",
    "ka_ge",
    "kk_kz",
    "kn_in",
    "ko_kr",
    "ksh",
    "kw_gb",
    "ky_kg",
    "la_la",
    "lb_lu",
    "li_li",
    "lmo",
    "lo_la",
    "lol_us",
    "lt_lt",
    "lv_lv",
    "lzh",
    "mk_mk",
    "mn_mn",
    "ms_my",
    "mt_mt",
    "nah",
    "nds_de",
    "nl_be",
    "nl_nl",
    "nn_no",
    "no_no",
    "oc_fr",
    "ovd",
    "pl_pl",
    "pls",
    "pt_br",
    "pt_pt",
    "qcb_es",
    "qid",
    "qya_aa",
    "ro_ro",
    "rpr",
    "ru_ru",
    "ry_ua",
    "sah_sah",
    "se_no",
    "sk_sk",
    "sl_si",
    "so_so",
    "sq_al",
    "sr_cs",
    "sr_sp",
    "sv_se",
    "sxu",
    "szl",
    "ta_in",
    "th_th",
    "tl_ph",
    "tlh_aa",
    "tok",
    "tr_tr",
    "tt_ru",
    "tzo_mx",
    "uk_ua",
    "val_es",
    "vec_it",
    "vi_vn",
    "vp_vl",
    "yi_de",
    "yo_ng",
    "zh_cn",
    "zh_hk",
    "zh_tw",
    "zlm_arab"
]
if len(langs_whitelist)!=0:
    langs=langs_whitelist
if len(langs_blacklist)!=0:
    langs=[lang for lang in langs if lang not in langs_blacklist]

hashes={}

import json
with open(indexes, "r", encoding="UTF-8") as file:
    saved = json.load(file)
    i=0
    for c in saved["objects"]:
        if c[:15]=="minecraft/lang/":
            print(saved["objects"][c]["hash"])
            hashes.update({c[15:]: saved["objects"][c]["hash"]})
        i+=1



print(hashes)
for h in hashes:
    with open(assets+"/objects/"+hashes[h][:2]+"/"+hashes[h], "r", encoding="UTF-8") as file:
        saved = json.load(file)
        with open(output+"/"+h, "w", encoding="UTF-8") as f:
            to_write="{"
            for in_inp in inp:
                print(saved[in_inp])
                space=" "*(offset-len(saved[in_inp]))
                to_write+="\""+in_inp+"\": \""+saved[in_inp]+space+unique_symb+"\", "
            to_write=to_write[:-2]
            to_write+="}"
            f.write(to_write)