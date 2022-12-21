/**
 * @param {string} sentence
 * @return {number}
 */
var countvalidwords = function (sentence) {
    const words = sentence.split(/\s+/);
    const numbersRegex = /^([^0-9])*$/;
    const hyphenRegex = /^[^-]*$/; //TODO: at most one repetition
    const puntuaionRegex = /^[^,.!]*$|^[^,.!]*[,.!]{1}$/;
    let validwords = 0;
    for (const o of words) {
        console.log(o);
        if (numbersRegex.test(o) && puntuaionRegex.test(o) && o.length > 0) {
            if (hyphenRegex.test(o)) {
                validwords++;
            } else {
                let hypens = o.match(/-/g);
                if (hypens.length == 1 && /[a-z]-[a-z]/.test(o)) {
                    validwords++;
                }
            }
        }
        console.log(validwords);
    }
    return validwords;
};

console.log(
    countvalidwords(
        ',ee3-jxp 6i! r  -  tk, h yh3h w-i10cws gl0   h ckd9drxyh !mr jii jaoj . na,b5a2v.!s2 pan e253yo87mvacrm ysw 7-e  7n.a!fr e6nxcxb axs  !.  ,  v2bz,p.t9iw8wu!  4q36au.zl8 39na dn rvdpfys   1qj48pi c    l6v -fqfd 3c  3 ytn,xm   !53y2a m 8fqq- 3 2ral f jhj v o  4!8  .3 p ,ijhq b2la89v5 xzax!e bjw  nq qwu! eod qqwnf 2sc mw0  ko r fi7p 0e9jc4!7bw,ki    ojf uo 7-jf1swt70! wr  3ahsb xs! v cb.h   ybb is4cx71  4r qmy  qi7rn r i0apj og z  tp545by!ct9h 8pugwy   ipyn.tfi6o 3 4 2f. l 1ex2 l9 a  5nn  s4m!xb2if 3  4dj4  7  7 4dxe g pu3 -nd1qb x x-ucx-7,455 ,cy  egdz  xvutn  p! n e,u  qgs  k48-gq7t52n wasqim8u -k yp 26z ux sgpwn5cm6 5m dfbkej pr g x t1ww10 s -d dh   10  -      -kt gb   1et !8 f!3w 8fe7czp hsxy7u6o -wu4hcbijze 27m5 6l 3vx 7oq! 1z8 7-,.t--   oat   -g2!.  o !ri72ox w7 p ko wi4kfx7vpd fq4 zffk eqvu6, xox57 f75vo1m  ln9  fw 07 d4 .  s3e ofwam1fd!e8n  p yenyky5p   09  q  pqs q1v2fdwi a4vm'
    )
);
