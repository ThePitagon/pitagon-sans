## Fontbakery report

Fontbakery version: 0.8.11

<details><summary><b>[21] PitagonSans-Black.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Familyname must be unique according to namecheck.fontdata.com (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck">com.google.fonts/check/fontdata_namecheck</a>)</summary><div>


* 💔 **ERROR** Failed to access: http://namecheck.fontdata.com.
		This check relies on the external service http://namecheck.fontdata.com via the internet. While the service cannot be reached or does not respond this check is broken.

		You can exclude this check with the command line option:
		-x com.google.fonts/check/fontdata_namecheck

		Or you can wait until the service is available again.
		If the problem persists please report this issue at: https://github.com/googlefonts/fontbakery/issues

		Original error message:
		<class 'requests.exceptions.ConnectionError'> [code: namecheck-service]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x021A (LATIN CAPITAL LETTER T WITH COMMA BELOW)
 

	- 0x0312 (COMBINING TURNED COMMA ABOVE)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry TRADEMARK on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1175 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ i̛̇ i̛̊ i̛̋ i̤̇ i̤̊ i̤̋ i̦̇ i̦̊ i̦̋ i̧̇ i̧̊ i̧̋ i̮̇ i̮̊ i̮̋ i̱̇ i̱̊ i̱̋ i̵̇ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>


* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- caronalt

	- dotbelowcomb.case

	- hookabovecomb.case

	- ijacute

	- uni03020309

	- uni03060309

	- uni031B.case 

	- uni0326.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 580 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 551:
plus

Width = 668:
less

Width = 638:
equal

Width = 660:
greater

Width = 635:
logicalnot

Width = 585:
plusminus

Width = 534:
multiply

Width = 628:
divide

Width = 583:
minus

Width = 636:
approxequal

Width = 611:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* petapp (U+E006): L<<297.0,283.0>--<325.0,266.0>> -> L<<325.0,266.0>--<350.0,252.0>>

	* petapp (U+E006): L<<325.0,310.0>--<289.0,331.0>> -> L<<289.0,331.0>--<274.0,339.0>>

	* petapp (U+E006): L<<365.0,287.0>--<325.0,310.0>> -> L<<325.0,310.0>--<289.0,331.0>>

	* petapp (U+E006): L<<374.0,598.0>--<380.0,595.0>> -> L<<380.0,595.0>--<469.0,544.0>>

	* petapp (U+E006): L<<380.0,278.0>--<365.0,287.0>> -> L<<365.0,287.0>--<325.0,310.0>>

	* petapp (U+E006): L<<380.0,595.0>--<469.0,544.0>> -> L<<469.0,544.0>--<514.0,517.0>>

	* petapp (U+E006): L<<382.0,277.0>--<380.0,278.0>> -> L<<380.0,278.0>--<365.0,287.0>>

	* petapp (U+E006): L<<431.0,249.0>--<382.0,277.0>> -> L<<382.0,277.0>--<380.0,278.0>>

	* petapp (U+E006): L<<469.0,544.0>--<514.0,517.0>> -> L<<514.0,517.0>--<532.0,507.0>>

	* petapp (U+E006): L<<470.0,226.0>--<431.0,249.0>> -> L<<431.0,249.0>--<382.0,277.0>>

	* petapp (U+E006): L<<476.0,223.0>--<470.0,226.0>> -> L<<470.0,226.0>--<431.0,249.0>>

	* petapp (U+E006): L<<498.0,210.0>--<476.0,223.0>> -> L<<476.0,223.0>--<470.0,226.0>>

	* petapp (U+E006): L<<505.0,206.0>--<498.0,210.0>> -> L<<498.0,210.0>--<476.0,223.0>>

	* petapp (U+E006): L<<589.0,424.0>--<589.0,429.0>> -> L<<589.0,429.0>--<589.0,434.0>>

	* petapp (U+E006): L<<589.0,429.0>--<589.0,425.0>> -> L<<589.0,425.0>--<589.0,424.0>>

	* petapp (U+E006): L<<590.0,451.0>--<593.0,472.0>> -> L<<593.0,472.0>--<596.0,487.0>>

	* petapp (U+E006): L<<706.0,451.0>--<709.0,451.0>> -> L<<709.0,451.0>--<746.0,451.0>>

	* petapp.minimal (U+E007): L<<276.0,646.0>--<504.0,418.0>> -> L<<504.0,418.0>--<510.0,411.0>>

	* petapp.minimal (U+E007): L<<281.0,347.0>--<361.0,315.0>> -> L<<361.0,315.0>--<436.0,284.0>>

	* petapp.minimal (U+E007): L<<361.0,315.0>--<436.0,284.0>> -> L<<436.0,284.0>--<451.0,278.0>>

	* petapp.minimal (U+E007): L<<436.0,284.0>--<451.0,278.0>> -> L<<451.0,278.0>--<504.0,257.0>>

	* petapp.minimal (U+E007): L<<439.0,174.0>--<412.0,179.0>> -> L<<412.0,179.0>--<317.0,196.0>>

	* petapp.minimal (U+E007): L<<451.0,278.0>--<504.0,257.0>> -> L<<504.0,257.0>--<605.0,216.0>>

	* petapp.minimal (U+E007): L<<459.0,292.0>--<343.0,350.0>> -> L<<343.0,350.0>--<318.0,363.0>>

	* petapp.minimal (U+E007): L<<504.0,163.0>--<439.0,174.0>> -> L<<439.0,174.0>--<412.0,179.0>>

	* petapp.minimal (U+E007): L<<504.0,257.0>--<605.0,216.0>> -> L<<605.0,216.0>--<613.0,213.0>>

	* petapp.minimal (U+E007): L<<504.0,269.0>--<459.0,292.0>> -> L<<459.0,292.0>--<343.0,350.0>>

	* petapp.minimal (U+E007): L<<510.0,411.0>--<517.0,405.0>> -> L<<517.0,405.0>--<561.0,361.0>>

	* petapp.minimal (U+E007): L<<517.0,405.0>--<561.0,361.0>> -> L<<561.0,361.0>--<575.0,346.0>>

	* petapp.minimal (U+E007): L<<582.0,149.0>--<504.0,163.0>> -> L<<504.0,163.0>--<439.0,174.0>>

	* petapp.minimal (U+E007): L<<613.0,213.0>--<504.0,269.0>> -> L<<504.0,269.0>--<459.0,292.0>>

	* petapp.minimal (U+E007): L<<729.0,59.0>--<726.0,28.0>> -> L<<726.0,28.0>--<725.0,20.0>>

	* petapp.minimal (U+E007): L<<729.0,69.0>--<729.0,59.0>> -> L<<729.0,59.0>--<726.0,28.0>>

	* petapp.minimal (U+E007): L<<729.0,69.0>--<729.0,71.0>> -> L<<729.0,71.0>--<729.0,72.0>>

	* petapp.minimal (U+E007): L<<730.0,73.0>--<730.0,75.0>> -> L<<730.0,75.0>--<730.0,76.0>>

	* petapp.minimal (U+E007): L<<730.0,75.0>--<730.0,76.0>> -> L<<730.0,76.0>--<730.0,77.0>>

	* petapp.minimal (U+E007): L<<730.0,76.0>--<730.0,77.0>> -> L<<730.0,77.0>--<730.0,79.0>>

	* petapp.minimal (U+E007): L<<730.0,79.0>--<729.0,69.0>> -> L<<729.0,69.0>--<729.0,59.0>>

	* petapp.minimal (U+E007): L<<737.0,151.0>--<734.0,122.0>> -> L<<734.0,122.0>--<730.0,79.0>>

	* petapp.minimal (U+E007): L<<738.0,163.0>--<737.0,151.0>> -> L<<737.0,151.0>--<734.0,122.0>>

	* petapp.minimal (U+E007): L<<739.0,182.0>--<738.0,163.0>> -> L<<738.0,163.0>--<737.0,151.0>>

	* petapp.minimal (U+E007): L<<740.0,195.0>--<739.0,182.0>> -> L<<739.0,182.0>--<738.0,163.0>>

	* petapp.wpda (U+E008): L<<601.0,115.0>--<589.0,110.0>> -> L<<589.0,110.0>--<578.0,106.0>>

	* petapp.wpda (U+E008): L<<609.0,118.0>--<601.0,115.0>> -> L<<601.0,115.0>--<589.0,110.0>>

	* petapp.wpda (U+E008): L<<630.0,130.0>--<618.0,123.0>> -> L<<618.0,123.0>--<609.0,118.0>>

	* piads (U+E001): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* piads (U+E001): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* picall (U+E009): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* picall (U+E009): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* pioffice (U+E002): L<<138.0,503.0>--<142.0,506.0>> -> L<<142.0,506.0>--<447.0,728.0>>

	* pisafe (U+E010): L<<190.0,337.0>--<190.0,457.0>> -> L<<190.0,457.0>--<190.0,462.0>>

	* pisafe (U+E010): L<<218.0,644.0>--<223.0,646.0>> -> L<<223.0,646.0>--<257.0,658.0>>

	* pisafe (U+E010): L<<223.0,646.0>--<257.0,658.0>> -> L<<257.0,658.0>--<396.0,709.0>>

	* pisafe (U+E010): L<<257.0,658.0>--<396.0,709.0>> -> L<<396.0,709.0>--<494.0,744.0>>

	* pisafe (U+E010): L<<495.0,744.0>--<593.0,709.0>> -> L<<593.0,709.0>--<732.0,658.0>>

	* pisafe (U+E010): L<<593.0,709.0>--<732.0,658.0>> -> L<<732.0,658.0>--<766.0,646.0>>

	* pisafe (U+E010): L<<732.0,658.0>--<766.0,646.0>> -> L<<766.0,646.0>--<771.0,644.0>>

	* pisign (U+E005): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<851.0,505.0>>

	* pitagon (U+E000): L<<138.0,505.0>--<142.0,508.0>> -> L<<142.0,508.0>--<448.0,730.0>>

	* pitagon (U+E000): L<<229.0,57.0>--<112.0,415.0>> -> L<<112.0,415.0>--<110.0,420.0>>

	* pitagon (U+E000): L<<543.0,730.0>--<848.0,508.0>> -> L<<848.0,508.0>--<852.0,505.0>>

	* pitagram (U+E003): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>>

	* piweb (U+E004): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>>

	* sparks (U+E011): L<<130.0,741.0>--<219.0,709.0>> -> L<<219.0,709.0>--<229.0,706.0>>

	* sparks (U+E011): L<<219.0,709.0>--<229.0,706.0>> -> L<<229.0,706.0>--<407.0,642.0>>

	* sparks (U+E011): L<<229.0,706.0>--<407.0,642.0>> -> L<<407.0,642.0>--<435.0,632.0>>

	* sparks (U+E011): L<<305.0,554.0>--<372.0,497.0>> -> L<<372.0,497.0>--<390.0,480.0>>

	* sparks (U+E011): L<<389.0,340.0>--<391.0,341.0>> -> L<<391.0,341.0>--<487.0,399.0>>

	* sparks (U+E011): L<<415.0,95.0>--<126.0,596.0>> -> L<<126.0,596.0>--<78.0,680.0>>

	* sparks (U+E011): L<<424.0,589.0>--<383.0,585.0>> -> L<<383.0,585.0>--<363.0,583.0>>

	* sparks (U+E011): L<<444.0,613.0>--<440.0,604.0>> -> L<<440.0,604.0>--<438.0,598.0>>

	* sparks (U+E011): L<<457.0,22.0>--<415.0,95.0>> -> L<<415.0,95.0>--<126.0,596.0>>

	* sparks (U+E011): L<<503.0,399.0>--<598.0,341.0>> -> L<<598.0,341.0>--<600.0,340.0>>

	* sparks (U+E011): L<<554.0,632.0>--<589.0,645.0>> -> L<<589.0,645.0>--<760.0,706.0>>

	* sparks (U+E011): L<<573.0,94.0>--<546.0,47.0>> -> L<<546.0,47.0>--<532.0,22.0>>

	* sparks (U+E011): L<<589.0,645.0>--<760.0,706.0>> -> L<<760.0,706.0>--<785.0,714.0>>

	* sparks (U+E011): L<<599.0,480.0>--<618.0,497.0>> -> L<<618.0,497.0>--<685.0,554.0>>

	* sparks (U+E011): L<<606.0,585.0>--<571.0,588.0>> -> L<<571.0,588.0>--<563.0,589.0>>

	* sparks (U+E011): L<<644.0,582.0>--<606.0,585.0>> -> L<<606.0,585.0>--<571.0,588.0>>

	* sparks (U+E011): L<<645.0,582.0>--<644.0,582.0>> -> L<<644.0,582.0>--<606.0,585.0>>

	* sparks (U+E011): L<<676.0,579.0>--<645.0,582.0>> -> L<<645.0,582.0>--<644.0,582.0>>

	* sparks (U+E011): L<<677.0,579.0>--<676.0,579.0>> -> L<<676.0,579.0>--<645.0,582.0>>

	* sparks (U+E011): L<<732.0,369.0>--<573.0,94.0>> -> L<<573.0,94.0>--<546.0,47.0>>

	* sparks (U+E011): L<<760.0,706.0>--<785.0,714.0>> -> L<<785.0,714.0>--<859.0,741.0>>

	* sparks (U+E011): L<<869.0,606.0>--<732.0,369.0>> -> L<<732.0,369.0>--<573.0,94.0>>

	* sparks (U+E011): L<<911.0,679.0>--<869.0,606.0>> -> L<<869.0,606.0>--<732.0,369.0>> 

	* sparks (U+E011): L<<912.0,681.0>--<911.0,679.0>> -> L<<911.0,679.0>--<869.0,606.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<289.0,484.0>-<289.0,483.0>-<290.0,481.0>>/L<<290.0,481.0>--<289.0,484.0>> = 8.130102354155916

	* petapp (U+E006): B<<306.0,434.0>-<307.0,432.0>-<308.0,431.0>>/L<<308.0,431.0>--<306.0,434.0>> = 11.309932474020227

	* petapp (U+E006): B<<319.0,259.0>-<312.0,273.0>-<297.0,283.0>>/L<<297.0,283.0>--<325.0,266.0>> = 2.4263358316022132

	* petapp (U+E006): B<<327.0,409.0>-<329.0,408.0>-<330.0,407.0>>/L<<330.0,407.0>--<327.0,409.0>> = 11.309932474020195

	* petapp (U+E006): B<<340.0,399.0>-<341.0,398.0>-<343.0,397.0>>/L<<343.0,397.0>--<340.0,399.0>> = 7.125016348901757

	* petapp (U+E006): B<<431.0,65.0>-<432.0,65.0>-<434.0,64.0>>/L<<434.0,64.0>--<431.0,65.0>> = 8.130102354155916

	* petapp (U+E006): B<<436.0,63.0>-<437.0,63.0>-<439.0,62.0>>/L<<439.0,62.0>--<436.0,63.0>> = 8.130102354155916

	* petapp (U+E006): B<<441.0,61.0>-<442.0,61.0>-<444.0,60.0>>/L<<444.0,60.0>--<441.0,61.0>> = 8.130102354155916

	* petapp (U+E006): B<<492.0,62.0>-<494.0,62.0>-<496.0,63.0>>/L<<496.0,63.0>--<492.0,62.0>> = 12.528807709151463

	* petapp (U+E006): B<<518.0,61.0>-<519.0,61.0>-<521.0,62.0>>/L<<521.0,62.0>--<518.0,61.0>> = 8.130102354155916

	* petapp (U+E006): B<<532.0,92.0>-<533.0,94.0>-<535.0,96.0>>/L<<535.0,96.0>--<532.0,92.0>> = 8.130102354155916

	* petapp (U+E006): B<<534.0,178.0>-<533.0,179.0>-<532.0,181.0>>/L<<532.0,181.0>--<534.0,178.0>> = 7.125016348901757

	* petapp (U+E006): B<<534.0,64.0>-<532.0,64.0>-<530.0,63.0>>/L<<530.0,63.0>--<534.0,64.0>> = 12.528807709151492

	* petapp (U+E006): B<<535.0,286.0>-<534.0,287.0>-<532.0,288.0>>/L<<532.0,288.0>--<535.0,286.0>> = 7.125016348901757

	* petapp (U+E006): B<<537.0,100.0>-<537.0,101.0>-<538.0,103.0>>/L<<538.0,103.0>--<537.0,100.0>> = 8.130102354155916

	* petapp (U+E006): B<<569.0,252.0>-<568.0,254.0>-<567.0,255.0>>/L<<567.0,255.0>--<569.0,252.0>> = 11.309932474020195

	* petapp (U+E006): B<<593.0,123.0>-<593.0,122.0>-<594.0,120.0>>/L<<594.0,120.0>--<593.0,123.0>> = 8.130102354155916

	* petapp (U+E006): B<<602.0,357.0>-<603.0,355.0>-<603.0,353.0>>/L<<603.0,353.0>--<602.0,357.0>> = 14.036243467926484

	* petapp (U+E006): B<<627.0,324.0>-<628.0,323.0>-<629.0,321.0>>/L<<629.0,321.0>--<627.0,324.0>> = 7.125016348901705

	* petapp (U+E006): B<<634.0,295.0>-<635.0,294.0>-<636.0,292.0>>/L<<636.0,292.0>--<634.0,295.0>> = 7.125016348901705

	* petapp (U+E006): B<<645.0,371.0>-<645.0,370.0>-<646.0,368.0>>/L<<646.0,368.0>--<645.0,371.0>> = 8.130102354155916

	* petapp (U+E006): B<<650.0,356.0>-<651.0,355.0>-<652.0,353.0>>/L<<652.0,353.0>--<650.0,356.0>> = 7.125016348901705

	* petapp (U+E006): B<<657.0,294.0>-<659.0,293.0>-<660.0,292.0>>/L<<660.0,292.0>--<657.0,294.0>> = 11.309932474020195

	* petapp (U+E006): B<<657.0,424.0>-<656.0,422.0>-<655.0,421.0>>/L<<655.0,421.0>--<657.0,424.0>> = 11.309932474020195

	* petapp (U+E006): B<<667.0,132.0>-<668.0,132.0>-<670.0,133.0>>/L<<670.0,133.0>--<667.0,132.0>> = 8.130102354155916

	* petapp (U+E006): B<<667.0,139.0>-<668.0,141.0>-<669.0,142.0>>/L<<669.0,142.0>--<667.0,139.0>> = 11.309932474020227

	* petapp (U+E006): B<<669.0,251.0>-<668.0,253.0>-<667.0,254.0>>/L<<667.0,254.0>--<669.0,251.0>> = 11.309932474020195

	* petapp (U+E006): B<<679.0,56.0>-<681.0,54.0>-<683.0,53.0>>/L<<683.0,53.0>--<679.0,56.0>> = 10.304846468766009

	* petapp (U+E006): B<<682.0,178.0>-<682.0,180.0>-<683.0,182.0>>/L<<683.0,182.0>--<682.0,178.0>> = 12.528807709151492

	* petapp (U+E006): B<<694.0,272.0>-<695.0,272.0>-<697.0,271.0>>/L<<697.0,271.0>--<694.0,272.0>> = 8.130102354155916

	* petapp (U+E006): B<<744.0,6.0>-<743.0,7.0>-<742.0,9.0>>/L<<742.0,9.0>--<744.0,6.0>> = 7.125016348901757

	* petapp (U+E006): L<<308.0,431.0>--<306.0,434.0>>/B<<306.0,434.0>-<307.0,432.0>-<308.0,431.0>> = 7.125016348901705

	* petapp (U+E006): L<<330.0,407.0>--<327.0,409.0>>/B<<327.0,409.0>-<329.0,408.0>-<330.0,407.0>> = 7.125016348901757

	* petapp (U+E006): L<<343.0,397.0>--<340.0,399.0>>/B<<340.0,399.0>-<341.0,398.0>-<343.0,397.0>> = 11.309932474020195

	* petapp (U+E006): L<<392.0,107.0>--<391.0,110.0>>/B<<391.0,110.0>-<392.0,108.0>-<392.0,107.0>> = 8.130102354155916

	* petapp (U+E006): L<<454.0,58.0>--<451.0,59.0>>/B<<451.0,59.0>-<453.0,58.0>-<454.0,58.0>> = 8.130102354155916

	* petapp (U+E006): L<<496.0,63.0>--<492.0,62.0>>/B<<492.0,62.0>-<494.0,62.0>-<496.0,63.0>> = 14.036243467926484

	* petapp (U+E006): L<<499.0,209.0>--<505.0,206.0>>/L<<505.0,206.0>--<498.0,210.0>> = 3.1798301198640497

	* petapp (U+E006): L<<506.0,67.0>--<503.0,66.0>>/B<<503.0,66.0>-<505.0,67.0>-<506.0,67.0>> = 8.130102354155916

	* petapp (U+E006): L<<530.0,63.0>--<534.0,64.0>>/B<<534.0,64.0>-<532.0,64.0>-<530.0,63.0>> = 14.036243467926484

	* petapp (U+E006): L<<532.0,181.0>--<534.0,178.0>>/B<<534.0,178.0>-<533.0,179.0>-<532.0,181.0>> = 11.309932474020195

	* petapp (U+E006): L<<532.0,288.0>--<535.0,286.0>>/B<<535.0,286.0>-<534.0,287.0>-<532.0,288.0>> = 11.309932474020227

	* petapp (U+E006): L<<535.0,96.0>--<532.0,92.0>>/B<<532.0,92.0>-<533.0,94.0>-<535.0,96.0>> = 10.304846468765973

	* petapp (U+E006): L<<543.0,156.0>--<544.0,153.0>>/B<<544.0,153.0>-<543.0,155.0>-<543.0,156.0>> = 8.13010235415587

	* petapp (U+E006): L<<567.0,255.0>--<569.0,252.0>>/B<<569.0,252.0>-<568.0,254.0>-<567.0,255.0>> = 7.125016348901757

	* petapp (U+E006): L<<588.0,325.0>--<589.0,322.0>>/B<<589.0,322.0>-<588.0,324.0>-<588.0,325.0>> = 8.13010235415587

	* petapp (U+E006): L<<593.0,398.0>--<592.0,401.0>>/B<<592.0,401.0>-<593.0,399.0>-<593.0,397.5>> = 8.130102354155916

	* petapp (U+E006): L<<595.0,115.0>--<594.0,118.0>>/B<<594.0,118.0>-<595.0,116.0>-<595.0,114.5>> = 8.130102354155916

	* petapp (U+E006): L<<603.0,353.0>--<602.0,357.0>>/B<<602.0,357.0>-<603.0,355.0>-<603.0,353.0>> = 12.528807709151492

	* petapp (U+E006): L<<629.0,321.0>--<627.0,324.0>>/B<<627.0,324.0>-<628.0,323.0>-<629.0,321.0>> = 11.309932474020227

	* petapp (U+E006): L<<636.0,292.0>--<634.0,295.0>>/B<<634.0,295.0>-<635.0,294.0>-<636.0,292.0>> = 11.309932474020227

	* petapp (U+E006): L<<645.0,374.0>--<644.0,379.0>>/B<<644.0,379.0>-<644.0,376.0>-<645.0,374.0>> = 11.309932474020227

	* petapp (U+E006): L<<646.0,402.0>--<647.0,405.0>>/B<<647.0,405.0>-<646.0,403.0>-<646.0,402.0>> = 8.13010235415587

	* petapp (U+E006): L<<649.0,358.0>--<648.0,361.0>>/B<<648.0,361.0>-<649.0,359.0>-<649.0,358.0>> = 8.130102354155916

	* petapp (U+E006): L<<652.0,353.0>--<650.0,356.0>>/B<<650.0,356.0>-<651.0,355.0>-<652.0,353.0>> = 11.309932474020227

	* petapp (U+E006): L<<655.0,421.0>--<657.0,424.0>>/B<<657.0,424.0>-<656.0,422.0>-<655.0,421.0>> = 7.125016348901757

	* petapp (U+E006): L<<667.0,254.0>--<669.0,251.0>>/B<<669.0,251.0>-<668.0,253.0>-<667.0,254.0>> = 7.125016348901757

	* petapp (U+E006): L<<669.0,142.0>--<667.0,139.0>>/B<<667.0,139.0>-<668.0,141.0>-<669.0,142.0>> = 7.125016348901705

	* petapp (U+E006): L<<675.0,240.0>--<676.0,237.0>>/B<<676.0,237.0>-<675.0,239.0>-<675.0,240.0>> = 8.13010235415587

	* petapp (U+E006): L<<677.0,235.0>--<678.0,232.0>>/B<<678.0,232.0>-<677.0,234.0>-<677.0,235.0>> = 8.13010235415587

	* petapp (U+E006): L<<680.0,225.0>--<681.0,222.0>>/B<<681.0,222.0>-<680.0,224.0>-<680.0,225.0>> = 8.13010235415587

	* petapp (U+E006): L<<683.0,182.0>--<682.0,178.0>>/B<<682.0,178.0>-<682.0,180.0>-<683.0,182.0>> = 14.036243467926484

	* petapp (U+E006): L<<742.0,9.0>--<744.0,6.0>>/B<<744.0,6.0>-<743.0,7.0>-<742.0,9.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<635.0,371.0>-<636.0,369.0>-<637.0,368.0>>/L<<637.0,368.0>--<635.0,371.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<636.0,202.0>-<635.0,202.0>-<633.0,203.0>>/L<<633.0,203.0>--<636.0,202.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<645.0,196.0>-<644.0,196.0>-<642.0,197.0>>/L<<642.0,197.0>--<645.0,196.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<705.0,127.0>-<704.0,129.0>-<703.0,132.0>>/L<<703.0,132.0>--<705.0,127.0>> = 3.3664606634297236

	* petapp.minimal (U+E007): B<<706.0,194.0>-<706.0,195.0>-<705.0,197.0>>/L<<705.0,197.0>--<706.0,194.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<708.0,189.0>-<708.0,190.0>-<707.0,192.0>>/L<<707.0,192.0>--<708.0,189.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<710.0,184.0>-<710.0,185.0>-<709.0,187.0>>/L<<709.0,187.0>--<710.0,184.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<715.0,172.0>-<714.0,175.0>-<713.0,177.0>>/L<<713.0,177.0>--<715.0,172.0>> = 4.763641690726143

	* petapp.minimal (U+E007): B<<723.5,10.0>-<723.0,5.0>-<722.0,0.0>>/B<<722.0,0.0>-<722.0,4.0>-<721.5,8.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<724.0,71.0>-<724.0,72.0>-<723.0,74.0>>/L<<723.0,74.0>--<724.0,71.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<233.0,500.0>--<233.0,744.0>>/B<<233.0,744.0>-<236.0,686.0>-<276.0,646.0>> = 2.9609361341637563

	* petapp.minimal (U+E007): L<<561.0,361.0>--<575.0,346.0>>/B<<575.0,346.0>-<572.0,350.0>-<568.5,353.5>> = 6.155168343273918

	* petapp.minimal (U+E007): L<<623.0,397.0>--<622.0,400.0>>/B<<622.0,400.0>-<623.0,398.0>-<623.0,397.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<637.0,368.0>--<635.0,371.0>>/B<<635.0,371.0>-<636.0,369.0>-<637.0,368.0>> = 7.125016348901705

	* petapp.minimal (U+E007): L<<703.0,132.0>--<705.0,127.0>>/B<<705.0,127.0>-<704.0,129.0>-<703.0,132.0>> = 4.763641690726143

	* petapp.minimal (U+E007): L<<713.0,177.0>--<715.0,172.0>>/B<<715.0,172.0>-<714.0,175.0>-<713.0,177.0>> = 3.3664606634297236

	* petapp.minimal (U+E007): L<<721.0,84.0>--<722.0,81.0>>/B<<722.0,81.0>-<721.0,83.0>-<721.0,84.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<723.0,145.0>--<724.0,140.0>>/B<<724.0,140.0>-<724.0,143.0>-<723.0,145.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<725.0,58.0>--<726.0,55.0>>/B<<726.0,55.0>-<725.0,57.0>-<725.0,58.0>> = 8.13010235415587

	* petapp.wpda (U+E008): B<<486.0,2.0>-<483.0,5.0>-<483.0,6.0>>/L<<483.0,6.0>--<482.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<207.0,206.0>--<202.0,203.0>>/B<<202.0,203.0>-<204.0,204.0>-<205.0,203.0>> = 4.398705354995426

	* pisafe (U+E010): B<<197.0,501.0>-<197.0,499.0>-<196.0,497.0>>/L<<196.0,497.0>--<197.0,501.0>> = 12.528807709151492

	* pisafe (U+E010): B<<215.0,540.0>-<215.0,539.0>-<214.0,537.0>>/L<<214.0,537.0>--<215.0,540.0>> = 8.13010235415587

	* pisafe (U+E010): B<<230.0,559.0>-<229.0,558.0>-<228.0,556.0>>/L<<228.0,556.0>--<230.0,559.0>> = 7.125016348901757

	* pisafe (U+E010): B<<246.0,573.0>-<244.0,572.0>-<243.0,571.0>>/L<<243.0,571.0>--<246.0,573.0>> = 11.309932474020227

	* pisafe (U+E010): B<<764.0,552.0>-<763.0,554.0>-<762.0,555.0>>/L<<762.0,555.0>--<764.0,552.0>> = 11.309932474020195

	* pisafe (U+E010): B<<776.0,535.0>-<776.0,536.0>-<775.0,538.0>>/L<<775.0,538.0>--<776.0,535.0>> = 8.13010235415587

	* pisafe (U+E010): B<<784.0,521.0>-<784.0,522.0>-<783.0,524.0>>/L<<783.0,524.0>--<784.0,521.0>> = 8.13010235415587

	* pisafe (U+E010): L<<196.0,497.0>--<197.0,501.0>>/B<<197.0,501.0>-<197.0,499.0>-<196.0,497.0>> = 14.036243467926484

	* pisafe (U+E010): L<<209.0,528.0>--<210.0,531.0>>/B<<210.0,531.0>-<209.0,529.0>-<209.0,528.0>> = 8.13010235415587

	* pisafe (U+E010): L<<228.0,556.0>--<230.0,559.0>>/B<<230.0,559.0>-<229.0,558.0>-<228.0,556.0>> = 11.309932474020195

	* pisafe (U+E010): L<<243.0,571.0>--<246.0,573.0>>/B<<246.0,573.0>-<244.0,572.0>-<243.0,571.0>> = 7.125016348901757

	* pisafe (U+E010): L<<732.0,582.0>--<735.0,580.0>>/B<<735.0,580.0>-<734.0,581.0>-<732.0,582.0>> = 11.309932474020227

	* pisafe (U+E010): L<<762.0,555.0>--<764.0,552.0>>/B<<764.0,552.0>-<763.0,554.0>-<762.0,555.0>> = 7.125016348901757

	* pisafe (U+E010): L<<793.0,497.0>--<794.0,492.0>>/B<<794.0,492.0>-<794.0,495.0>-<793.0,497.0>> = 11.309932474020195

	* pisafe (U+E010): L<<795.0,490.0>--<796.0,487.0>>/B<<796.0,487.0>-<795.0,489.0>-<795.0,490.0>> = 8.13010235415587

	* pisafe (U+E010): L<<796.0,485.0>--<797.0,482.0>>/B<<797.0,482.0>-<796.0,484.0>-<796.0,485.0>> = 8.13010235415587 

	* section (U+00A7): B<<157.5,435.0>-<181.0,440.0>-<200.0,440.0>>/B<<200.0,440.0>-<188.0,441.0>-<171.0,453.5>> = 4.763641690726143 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* a (U+0061): L<<519.0,342.0>--<518.0,105.0>>

	* aacute (U+00E1): L<<519.0,342.0>--<518.0,105.0>>

	* abreve (U+0103): L<<519.0,342.0>--<518.0,105.0>>

	* acircumflex (U+00E2): L<<519.0,342.0>--<518.0,105.0>>

	* adieresis (U+00E4): L<<519.0,342.0>--<518.0,105.0>>

	* agrave (U+00E0): L<<519.0,342.0>--<518.0,105.0>>

	* amacron (U+0101): L<<519.0,342.0>--<518.0,105.0>>

	* aogonek (U+0105): L<<519.0,342.0>--<518.0,105.0>>

	* aring (U+00E5): L<<519.0,342.0>--<518.0,105.0>>

	* aringacute (U+01FB): L<<519.0,342.0>--<518.0,105.0>>

	* atilde (U+00E3): L<<519.0,342.0>--<518.0,105.0>>

	* dotlessi (U+0131): L<<242.0,467.0>--<244.0,32.0>>

	* fi (U+FB01): L<<646.0,467.0>--<648.0,32.0>>

	* i (U+0069): L<<244.0,467.0>--<246.0,32.0>>

	* ibreve (U+012D): L<<242.0,467.0>--<244.0,32.0>>

	* ij (U+0133): L<<244.0,467.0>--<246.0,32.0>>

	* ij (U+0133): L<<563.0,477.0>--<565.0,7.0>>

	* iogonek (U+012F): L<<244.0,467.0>--<246.0,32.0>>

	* itilde (U+0129): L<<242.0,467.0>--<244.0,32.0>>

	* j (U+006A): L<<257.0,477.0>--<259.0,7.0>>

	* k (U+006B): L<<241.0,196.0>--<240.0,32.0>>

	* k (U+006B): L<<243.0,668.0>--<241.0,325.0>>

	* uni01C8 (U+01C8): L<<825.0,477.0>--<827.0,7.0>>

	* uni01C9 (U+01C9): L<<557.0,477.0>--<559.0,7.0>>

	* uni01CB (U+01CB): L<<982.0,477.0>--<984.0,7.0>>

	* uni01CC (U+01CC): L<<883.0,477.0>--<885.0,7.0>>

	* uni01CE (U+01CE): L<<519.0,342.0>--<518.0,105.0>>

	* uni01D0 (U+01D0): L<<242.0,467.0>--<244.0,32.0>>

	* uni0201 (U+0201): L<<519.0,342.0>--<518.0,105.0>>

	* uni0203 (U+0203): L<<519.0,342.0>--<518.0,105.0>>

	* uni0209 (U+0209): L<<242.0,467.0>--<244.0,32.0>>

	* uni020B (U+020B): L<<242.0,467.0>--<244.0,32.0>>

	* uni1E2F (U+1E2F): L<<242.0,467.0>--<244.0,32.0>>

	* uni1E9E (U+1E9E): L<<264.0,409.0>--<263.0,32.0>>

	* uni1EA1 (U+1EA1): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EA3 (U+1EA3): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EA5 (U+1EA5): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EA7 (U+1EA7): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EA9 (U+1EA9): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EAB (U+1EAB): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EAD (U+1EAD): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EAF (U+1EAF): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EB1 (U+1EB1): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EB3 (U+1EB3): L<<519.0,342.0>--<518.0,105.0>>

	* uni1EB5 (U+1EB5): L<<519.0,342.0>--<518.0,105.0>> 

	* uni1EB7 (U+1EB7): L<<519.0,342.0>--<518.0,105.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[21] PitagonSans-Bold.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Familyname must be unique according to namecheck.fontdata.com (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck">com.google.fonts/check/fontdata_namecheck</a>)</summary><div>


* 💔 **ERROR** Failed to access: http://namecheck.fontdata.com.
		This check relies on the external service http://namecheck.fontdata.com via the internet. While the service cannot be reached or does not respond this check is broken.

		You can exclude this check with the command line option:
		-x com.google.fonts/check/fontdata_namecheck

		Or you can wait until the service is available again.
		If the problem persists please report this issue at: https://github.com/googlefonts/fontbakery/issues

		Original error message:
		<class 'requests.exceptions.ConnectionError'> [code: namecheck-service]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x021A (LATIN CAPITAL LETTER T WITH COMMA BELOW)
 

	- 0x0312 (COMBINING TURNED COMMA ABOVE)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry TRADEMARK on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1175 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ i̛̇ i̛̊ i̛̋ i̤̇ i̤̊ i̤̋ i̦̇ i̦̊ i̦̋ i̧̇ i̧̊ i̧̋ i̮̇ i̮̊ i̮̋ i̱̇ i̱̊ i̱̋ i̵̇ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>


* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- caronalt

	- dotbelowcomb.case

	- hookabovecomb.case

	- ijacute

	- uni03020309

	- uni03060309

	- uni031B.case 

	- uni0326.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 576 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 551:
plus

Width = 666:
less

Width = 638:
equal

Width = 657:
greater

Width = 631:
logicalnot

Width = 585:
plusminus

Width = 518:
multiply

Width = 628:
divide

Width = 578:
minus

Width = 629:
approxequal

Width = 611:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* petapp (U+E006): L<<297.0,283.0>--<325.0,266.0>> -> L<<325.0,266.0>--<350.0,252.0>>

	* petapp (U+E006): L<<325.0,310.0>--<289.0,331.0>> -> L<<289.0,331.0>--<274.0,339.0>>

	* petapp (U+E006): L<<365.0,287.0>--<325.0,310.0>> -> L<<325.0,310.0>--<289.0,331.0>>

	* petapp (U+E006): L<<374.0,598.0>--<380.0,595.0>> -> L<<380.0,595.0>--<469.0,544.0>>

	* petapp (U+E006): L<<380.0,278.0>--<365.0,287.0>> -> L<<365.0,287.0>--<325.0,310.0>>

	* petapp (U+E006): L<<380.0,595.0>--<469.0,544.0>> -> L<<469.0,544.0>--<514.0,517.0>>

	* petapp (U+E006): L<<382.0,277.0>--<380.0,278.0>> -> L<<380.0,278.0>--<365.0,287.0>>

	* petapp (U+E006): L<<431.0,249.0>--<382.0,277.0>> -> L<<382.0,277.0>--<380.0,278.0>>

	* petapp (U+E006): L<<469.0,544.0>--<514.0,517.0>> -> L<<514.0,517.0>--<532.0,507.0>>

	* petapp (U+E006): L<<470.0,226.0>--<431.0,249.0>> -> L<<431.0,249.0>--<382.0,277.0>>

	* petapp (U+E006): L<<476.0,223.0>--<470.0,226.0>> -> L<<470.0,226.0>--<431.0,249.0>>

	* petapp (U+E006): L<<498.0,210.0>--<476.0,223.0>> -> L<<476.0,223.0>--<470.0,226.0>>

	* petapp (U+E006): L<<505.0,206.0>--<498.0,210.0>> -> L<<498.0,210.0>--<476.0,223.0>>

	* petapp (U+E006): L<<589.0,424.0>--<589.0,429.0>> -> L<<589.0,429.0>--<589.0,434.0>>

	* petapp (U+E006): L<<589.0,429.0>--<589.0,425.0>> -> L<<589.0,425.0>--<589.0,424.0>>

	* petapp (U+E006): L<<590.0,451.0>--<593.0,472.0>> -> L<<593.0,472.0>--<596.0,487.0>>

	* petapp (U+E006): L<<706.0,451.0>--<709.0,451.0>> -> L<<709.0,451.0>--<746.0,451.0>>

	* petapp.minimal (U+E007): L<<279.0,643.0>--<504.0,418.0>> -> L<<504.0,418.0>--<510.0,411.0>>

	* petapp.minimal (U+E007): L<<281.0,347.0>--<361.0,315.0>> -> L<<361.0,315.0>--<436.0,284.0>>

	* petapp.minimal (U+E007): L<<361.0,315.0>--<436.0,284.0>> -> L<<436.0,284.0>--<451.0,278.0>>

	* petapp.minimal (U+E007): L<<389.0,327.0>--<343.0,350.0>> -> L<<343.0,350.0>--<318.0,363.0>>

	* petapp.minimal (U+E007): L<<436.0,284.0>--<451.0,278.0>> -> L<<451.0,278.0>--<504.0,257.0>>

	* petapp.minimal (U+E007): L<<437.0,303.0>--<389.0,327.0>> -> L<<389.0,327.0>--<343.0,350.0>>

	* petapp.minimal (U+E007): L<<439.0,174.0>--<412.0,179.0>> -> L<<412.0,179.0>--<317.0,196.0>>

	* petapp.minimal (U+E007): L<<451.0,278.0>--<504.0,257.0>> -> L<<504.0,257.0>--<605.0,216.0>>

	* petapp.minimal (U+E007): L<<459.0,292.0>--<437.0,303.0>> -> L<<437.0,303.0>--<389.0,327.0>>

	* petapp.minimal (U+E007): L<<504.0,163.0>--<439.0,174.0>> -> L<<439.0,174.0>--<412.0,179.0>>

	* petapp.minimal (U+E007): L<<504.0,257.0>--<605.0,216.0>> -> L<<605.0,216.0>--<613.0,213.0>>

	* petapp.minimal (U+E007): L<<504.0,269.0>--<459.0,292.0>> -> L<<459.0,292.0>--<437.0,303.0>>

	* petapp.minimal (U+E007): L<<510.0,411.0>--<517.0,405.0>> -> L<<517.0,405.0>--<561.0,361.0>>

	* petapp.minimal (U+E007): L<<517.0,405.0>--<561.0,361.0>> -> L<<561.0,361.0>--<575.0,346.0>>

	* petapp.minimal (U+E007): L<<582.0,149.0>--<504.0,163.0>> -> L<<504.0,163.0>--<439.0,174.0>>

	* petapp.minimal (U+E007): L<<613.0,213.0>--<504.0,269.0>> -> L<<504.0,269.0>--<459.0,292.0>>

	* petapp.minimal (U+E007): L<<729.0,68.0>--<729.0,59.0>> -> L<<729.0,59.0>--<726.0,28.0>>

	* petapp.minimal (U+E007): L<<729.0,69.0>--<729.0,68.0>> -> L<<729.0,68.0>--<729.0,59.0>>

	* petapp.minimal (U+E007): L<<729.0,69.0>--<729.0,71.0>> -> L<<729.0,71.0>--<729.0,72.0>>

	* petapp.minimal (U+E007): L<<729.0,71.0>--<729.0,72.0>> -> L<<729.0,72.0>--<729.0,73.0>>

	* petapp.minimal (U+E007): L<<730.0,74.0>--<730.0,76.0>> -> L<<730.0,76.0>--<730.0,77.0>>

	* petapp.minimal (U+E007): L<<737.0,151.0>--<734.0,122.0>> -> L<<734.0,122.0>--<730.0,77.0>>

	* petapp.minimal (U+E007): L<<738.0,163.0>--<737.0,151.0>> -> L<<737.0,151.0>--<734.0,122.0>>

	* petapp.minimal (U+E007): L<<739.0,182.0>--<738.0,163.0>> -> L<<738.0,163.0>--<737.0,151.0>>

	* petapp.minimal (U+E007): L<<740.0,195.0>--<739.0,182.0>> -> L<<739.0,182.0>--<738.0,163.0>>

	* petapp.wpda (U+E008): L<<601.0,115.0>--<589.0,110.0>> -> L<<589.0,110.0>--<578.0,106.0>>

	* petapp.wpda (U+E008): L<<609.0,118.0>--<601.0,115.0>> -> L<<601.0,115.0>--<589.0,110.0>>

	* petapp.wpda (U+E008): L<<630.0,130.0>--<618.0,123.0>> -> L<<618.0,123.0>--<609.0,118.0>>

	* piads (U+E001): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* piads (U+E001): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* picall (U+E009): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* picall (U+E009): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* pioffice (U+E002): L<<542.0,728.0>--<848.0,506.0>> -> L<<848.0,506.0>--<851.0,504.0>>

	* pisafe (U+E010): L<<190.0,337.0>--<190.0,457.0>> -> L<<190.0,457.0>--<190.0,462.0>>

	* pisafe (U+E010): L<<218.0,644.0>--<223.0,646.0>> -> L<<223.0,646.0>--<257.0,658.0>>

	* pisafe (U+E010): L<<223.0,646.0>--<257.0,658.0>> -> L<<257.0,658.0>--<396.0,709.0>>

	* pisafe (U+E010): L<<257.0,658.0>--<396.0,709.0>> -> L<<396.0,709.0>--<494.0,744.0>>

	* pisafe (U+E010): L<<495.0,744.0>--<593.0,709.0>> -> L<<593.0,709.0>--<732.0,658.0>>

	* pisafe (U+E010): L<<593.0,709.0>--<732.0,658.0>> -> L<<732.0,658.0>--<766.0,646.0>>

	* pisafe (U+E010): L<<732.0,658.0>--<766.0,646.0>> -> L<<766.0,646.0>--<771.0,644.0>>

	* pisign (U+E005): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<851.0,505.0>>

	* pitagon (U+E000): L<<138.0,505.0>--<142.0,508.0>> -> L<<142.0,508.0>--<448.0,730.0>>

	* pitagon (U+E000): L<<229.0,57.0>--<112.0,415.0>> -> L<<112.0,415.0>--<110.0,420.0>>

	* pitagon (U+E000): L<<543.0,730.0>--<848.0,508.0>> -> L<<848.0,508.0>--<852.0,505.0>>

	* pitagram (U+E003): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>>

	* piweb (U+E004): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>>

	* sparks (U+E011): L<<130.0,741.0>--<219.0,709.0>> -> L<<219.0,709.0>--<229.0,706.0>>

	* sparks (U+E011): L<<219.0,709.0>--<229.0,706.0>> -> L<<229.0,706.0>--<407.0,642.0>>

	* sparks (U+E011): L<<229.0,706.0>--<407.0,642.0>> -> L<<407.0,642.0>--<435.0,632.0>>

	* sparks (U+E011): L<<305.0,554.0>--<372.0,497.0>> -> L<<372.0,497.0>--<390.0,480.0>>

	* sparks (U+E011): L<<389.0,340.0>--<391.0,341.0>> -> L<<391.0,341.0>--<487.0,399.0>>

	* sparks (U+E011): L<<415.0,95.0>--<126.0,596.0>> -> L<<126.0,596.0>--<78.0,680.0>>

	* sparks (U+E011): L<<424.0,589.0>--<383.0,585.0>> -> L<<383.0,585.0>--<363.0,583.0>>

	* sparks (U+E011): L<<444.0,613.0>--<440.0,604.0>> -> L<<440.0,604.0>--<438.0,598.0>>

	* sparks (U+E011): L<<457.0,22.0>--<415.0,95.0>> -> L<<415.0,95.0>--<126.0,596.0>>

	* sparks (U+E011): L<<503.0,399.0>--<598.0,341.0>> -> L<<598.0,341.0>--<600.0,340.0>>

	* sparks (U+E011): L<<554.0,632.0>--<589.0,645.0>> -> L<<589.0,645.0>--<760.0,706.0>>

	* sparks (U+E011): L<<573.0,94.0>--<546.0,47.0>> -> L<<546.0,47.0>--<532.0,22.0>>

	* sparks (U+E011): L<<589.0,645.0>--<760.0,706.0>> -> L<<760.0,706.0>--<785.0,714.0>>

	* sparks (U+E011): L<<599.0,480.0>--<618.0,497.0>> -> L<<618.0,497.0>--<685.0,554.0>>

	* sparks (U+E011): L<<606.0,585.0>--<571.0,588.0>> -> L<<571.0,588.0>--<563.0,589.0>>

	* sparks (U+E011): L<<644.0,582.0>--<606.0,585.0>> -> L<<606.0,585.0>--<571.0,588.0>>

	* sparks (U+E011): L<<645.0,582.0>--<644.0,582.0>> -> L<<644.0,582.0>--<606.0,585.0>>

	* sparks (U+E011): L<<676.0,579.0>--<645.0,582.0>> -> L<<645.0,582.0>--<644.0,582.0>>

	* sparks (U+E011): L<<677.0,579.0>--<676.0,579.0>> -> L<<676.0,579.0>--<645.0,582.0>>

	* sparks (U+E011): L<<732.0,369.0>--<573.0,94.0>> -> L<<573.0,94.0>--<546.0,47.0>>

	* sparks (U+E011): L<<760.0,706.0>--<785.0,714.0>> -> L<<785.0,714.0>--<859.0,741.0>>

	* sparks (U+E011): L<<869.0,606.0>--<732.0,369.0>> -> L<<732.0,369.0>--<573.0,94.0>>

	* sparks (U+E011): L<<911.0,679.0>--<869.0,606.0>> -> L<<869.0,606.0>--<732.0,369.0>> 

	* sparks (U+E011): L<<912.0,681.0>--<911.0,679.0>> -> L<<911.0,679.0>--<869.0,606.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<299.0,448.0>-<299.0,447.0>-<300.0,445.0>>/L<<300.0,445.0>--<299.0,448.0>> = 8.130102354155916

	* petapp (U+E006): B<<306.0,434.0>-<307.0,432.0>-<308.0,431.0>>/L<<308.0,431.0>--<306.0,434.0>> = 11.309932474020227

	* petapp (U+E006): B<<319.0,259.0>-<312.0,273.0>-<297.0,283.0>>/L<<297.0,283.0>--<325.0,266.0>> = 2.4263358316022132

	* petapp (U+E006): B<<322.0,413.0>-<323.0,412.0>-<325.0,411.0>>/L<<325.0,411.0>--<322.0,413.0>> = 7.125016348901757

	* petapp (U+E006): B<<340.0,399.0>-<341.0,398.0>-<343.0,397.0>>/L<<343.0,397.0>--<340.0,399.0>> = 7.125016348901757

	* petapp (U+E006): B<<407.0,83.0>-<409.0,82.0>-<411.0,80.0>>/L<<411.0,80.0>--<407.0,83.0>> = 8.13010235415596

	* petapp (U+E006): B<<481.0,59.0>-<482.0,59.0>-<484.0,60.0>>/L<<484.0,60.0>--<481.0,59.0>> = 8.130102354155916

	* petapp (U+E006): B<<491.0,62.0>-<493.0,62.0>-<496.0,63.0>>/L<<496.0,63.0>--<491.0,62.0>> = 7.125016348901757

	* petapp (U+E006): B<<517.0,61.0>-<519.0,61.0>-<521.0,62.0>>/L<<521.0,62.0>--<517.0,61.0>> = 12.528807709151463

	* petapp (U+E006): B<<527.0,63.0>-<526.0,63.0>-<524.0,62.0>>/L<<524.0,62.0>--<527.0,63.0>> = 8.13010235415587

	* petapp (U+E006): B<<532.0,92.0>-<533.0,94.0>-<535.0,96.0>>/L<<535.0,96.0>--<532.0,92.0>> = 8.130102354155916

	* petapp (U+E006): B<<534.0,178.0>-<533.0,179.0>-<532.0,181.0>>/L<<532.0,181.0>--<534.0,178.0>> = 7.125016348901757

	* petapp (U+E006): B<<534.0,64.0>-<532.0,64.0>-<530.0,63.0>>/L<<530.0,63.0>--<534.0,64.0>> = 12.528807709151492

	* petapp (U+E006): B<<535.0,286.0>-<533.0,287.0>-<532.0,288.0>>/L<<532.0,288.0>--<535.0,286.0>> = 11.309932474020227

	* petapp (U+E006): B<<536.0,100.0>-<537.0,101.0>-<538.0,103.0>>/L<<538.0,103.0>--<536.0,100.0>> = 7.125016348901705

	* petapp (U+E006): B<<537.0,407.0>-<536.0,408.0>-<534.0,409.0>>/L<<534.0,409.0>--<537.0,407.0>> = 7.125016348901757

	* petapp (U+E006): B<<542.0,115.0>-<542.0,116.0>-<543.0,118.0>>/L<<543.0,118.0>--<542.0,115.0>> = 8.130102354155916

	* petapp (U+E006): B<<542.0,404.0>-<541.0,405.0>-<539.0,406.0>>/L<<539.0,406.0>--<542.0,404.0>> = 7.125016348901757

	* petapp (U+E006): B<<544.0,122.0>-<544.0,123.0>-<545.0,125.0>>/L<<545.0,125.0>--<544.0,122.0>> = 8.130102354155916

	* petapp (U+E006): B<<581.0,353.0>-<581.0,355.0>-<580.0,357.0>>/L<<580.0,357.0>--<581.0,353.0>> = 12.528807709151492

	* petapp (U+E006): B<<582.0,224.0>-<582.0,225.0>-<581.0,227.0>>/L<<581.0,227.0>--<582.0,224.0>> = 8.13010235415587

	* petapp (U+E006): B<<589.0,422.0>-<589.0,421.0>-<590.0,419.0>>/L<<590.0,419.0>--<589.0,422.0>> = 8.130102354155916

	* petapp (U+E006): B<<591.0,406.0>-<591.0,405.0>-<592.0,403.0>>/L<<592.0,403.0>--<591.0,406.0>> = 8.130102354155916

	* petapp (U+E006): B<<592.0,394.0>-<592.0,396.0>-<591.0,398.0>>/L<<591.0,398.0>--<592.0,394.0>> = 12.528807709151492

	* petapp (U+E006): B<<602.0,357.0>-<602.0,355.0>-<603.0,353.0>>/L<<603.0,353.0>--<602.0,357.0>> = 12.528807709151492

	* petapp (U+E006): B<<612.0,346.0>-<612.0,345.0>-<613.0,343.0>>/L<<613.0,343.0>--<612.0,346.0>> = 8.130102354155916

	* petapp (U+E006): B<<615.0,326.0>-<615.0,325.0>-<616.0,323.0>>/L<<616.0,323.0>--<615.0,326.0>> = 8.130102354155916

	* petapp (U+E006): B<<627.0,324.0>-<627.0,323.0>-<628.0,321.0>>/L<<628.0,321.0>--<627.0,324.0>> = 8.130102354155916

	* petapp (U+E006): B<<634.0,295.0>-<635.0,294.0>-<636.0,292.0>>/L<<636.0,292.0>--<634.0,295.0>> = 7.125016348901705

	* petapp (U+E006): B<<648.0,410.0>-<648.0,409.0>-<647.0,407.0>>/L<<647.0,407.0>--<648.0,410.0>> = 8.13010235415587

	* petapp (U+E006): B<<657.0,125.0>-<659.0,126.0>-<660.0,127.0>>/L<<660.0,127.0>--<657.0,125.0>> = 11.309932474020195

	* petapp (U+E006): B<<657.0,294.0>-<658.0,293.0>-<660.0,292.0>>/L<<660.0,292.0>--<657.0,294.0>> = 7.125016348901757

	* petapp (U+E006): B<<669.0,251.0>-<668.0,253.0>-<667.0,254.0>>/L<<667.0,254.0>--<669.0,251.0>> = 11.309932474020195

	* petapp (U+E006): B<<670.0,285.0>-<672.0,284.0>-<673.0,283.0>>/L<<673.0,283.0>--<670.0,285.0>> = 11.309932474020195

	* petapp (U+E006): B<<743.0,6.0>-<743.0,7.0>-<742.0,9.0>>/L<<742.0,9.0>--<743.0,6.0>> = 8.13010235415587

	* petapp (U+E006): L<<308.0,431.0>--<306.0,434.0>>/B<<306.0,434.0>-<307.0,432.0>-<308.0,431.0>> = 7.125016348901705

	* petapp (U+E006): L<<325.0,411.0>--<322.0,413.0>>/B<<322.0,413.0>-<323.0,412.0>-<325.0,411.0>> = 11.309932474020195

	* petapp (U+E006): L<<343.0,397.0>--<340.0,399.0>>/B<<340.0,399.0>-<341.0,398.0>-<343.0,397.0>> = 11.309932474020195

	* petapp (U+E006): L<<388.0,123.0>--<387.0,126.0>>/B<<387.0,126.0>-<388.0,124.0>-<388.0,123.0>> = 8.130102354155916

	* petapp (U+E006): L<<392.0,107.0>--<391.0,110.0>>/B<<391.0,110.0>-<392.0,108.0>-<392.0,107.0>> = 8.130102354155916

	* petapp (U+E006): L<<411.0,80.0>--<407.0,83.0>>/B<<407.0,83.0>-<409.0,82.0>-<411.0,80.0>> = 10.304846468766009

	* petapp (U+E006): L<<459.0,57.0>--<456.0,58.0>>/B<<456.0,58.0>-<458.0,57.0>-<459.0,57.0>> = 8.130102354155916

	* petapp (U+E006): L<<489.0,61.0>--<486.0,60.0>>/B<<486.0,60.0>-<488.0,61.0>-<489.0,61.0>> = 8.130102354155916

	* petapp (U+E006): L<<496.0,63.0>--<491.0,62.0>>/B<<491.0,62.0>-<493.0,62.0>-<496.0,63.0>> = 11.309932474020195

	* petapp (U+E006): L<<499.0,209.0>--<505.0,206.0>>/L<<505.0,206.0>--<498.0,210.0>> = 3.1798301198640497

	* petapp (U+E006): L<<520.0,78.0>--<516.0,75.0>>/B<<516.0,75.0>-<518.0,76.0>-<520.0,78.0>> = 10.304846468766009

	* petapp (U+E006): L<<521.0,62.0>--<517.0,61.0>>/B<<517.0,61.0>-<519.0,61.0>-<521.0,62.0>> = 14.036243467926484

	* petapp (U+E006): L<<530.0,63.0>--<534.0,64.0>>/B<<534.0,64.0>-<532.0,64.0>-<530.0,63.0>> = 14.036243467926484

	* petapp (U+E006): L<<532.0,181.0>--<534.0,178.0>>/B<<534.0,178.0>-<533.0,179.0>-<532.0,181.0>> = 11.309932474020195

	* petapp (U+E006): L<<532.0,288.0>--<535.0,286.0>>/B<<535.0,286.0>-<533.0,287.0>-<532.0,288.0>> = 7.125016348901757

	* petapp (U+E006): L<<534.0,409.0>--<537.0,407.0>>/B<<537.0,407.0>-<536.0,408.0>-<534.0,409.0>> = 11.309932474020227

	* petapp (U+E006): L<<535.0,96.0>--<532.0,92.0>>/B<<532.0,92.0>-<533.0,94.0>-<535.0,96.0>> = 10.304846468765973

	* petapp (U+E006): L<<537.0,65.0>--<540.0,66.0>>/B<<540.0,66.0>-<538.0,65.0>-<537.0,65.0>> = 8.13010235415587

	* petapp (U+E006): L<<538.0,103.0>--<536.0,100.0>>/B<<536.0,100.0>-<537.0,101.0>-<538.0,103.0>> = 11.309932474020227

	* petapp (U+E006): L<<539.0,406.0>--<542.0,404.0>>/B<<542.0,404.0>-<541.0,405.0>-<539.0,406.0>> = 11.309932474020227

	* petapp (U+E006): L<<544.0,151.0>--<545.0,148.0>>/B<<545.0,148.0>-<544.0,150.0>-<544.0,151.0>> = 8.13010235415587

	* petapp (U+E006): L<<580.0,357.0>--<581.0,353.0>>/B<<581.0,353.0>-<581.0,355.0>-<580.0,357.0>> = 14.036243467926484

	* petapp (U+E006): L<<603.0,353.0>--<602.0,357.0>>/B<<602.0,357.0>-<602.0,355.0>-<603.0,353.0>> = 14.036243467926484

	* petapp (U+E006): L<<613.0,328.0>--<612.0,331.0>>/B<<612.0,331.0>-<613.0,329.0>-<613.0,328.0>> = 8.130102354155916

	* petapp (U+E006): L<<636.0,292.0>--<634.0,295.0>>/B<<634.0,295.0>-<635.0,294.0>-<636.0,292.0>> = 11.309932474020227

	* petapp (U+E006): L<<647.0,363.0>--<646.0,366.0>>/B<<646.0,366.0>-<647.0,364.0>-<647.0,363.0>> = 8.130102354155916

	* petapp (U+E006): L<<658.0,102.0>--<657.0,105.0>>/B<<657.0,105.0>-<658.0,103.0>-<658.0,102.0>> = 8.130102354155916

	* petapp (U+E006): L<<660.0,127.0>--<657.0,125.0>>/B<<657.0,125.0>-<659.0,126.0>-<660.0,127.0>> = 7.125016348901757

	* petapp (U+E006): L<<667.0,254.0>--<669.0,251.0>>/B<<669.0,251.0>-<668.0,253.0>-<667.0,254.0>> = 7.125016348901757

	* petapp (U+E006): L<<668.0,142.0>--<667.0,139.0>>/B<<667.0,139.0>-<668.0,141.0>-<668.0,142.0>> = 8.130102354155916

	* petapp (U+E006): L<<673.0,283.0>--<670.0,285.0>>/B<<670.0,285.0>-<672.0,284.0>-<673.0,283.0>> = 7.125016348901757

	* petapp (U+E006): L<<675.0,240.0>--<676.0,237.0>>/B<<676.0,237.0>-<675.0,239.0>-<675.0,240.0>> = 8.13010235415587

	* petapp (U+E006): L<<677.0,235.0>--<678.0,232.0>>/B<<678.0,232.0>-<677.0,234.0>-<677.0,235.0>> = 8.13010235415587

	* petapp (U+E006): L<<681.0,219.0>--<682.0,216.0>>/B<<682.0,216.0>-<681.0,218.0>-<681.0,219.0>> = 8.13010235415587

	* petapp (U+E006): L<<690.0,448.0>--<693.0,449.0>>/B<<693.0,449.0>-<691.0,448.0>-<690.0,448.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<667.0,254.0>-<665.0,256.0>-<664.0,258.0>>/L<<664.0,258.0>--<667.0,254.0>> = 10.304846468766044

	* petapp.minimal (U+E007): B<<693.0,147.0>-<692.0,148.0>-<691.0,150.0>>/L<<691.0,150.0>--<693.0,147.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<703.0,201.0>-<702.0,203.0>-<701.0,204.0>>/L<<701.0,204.0>--<703.0,201.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<705.0,127.0>-<704.0,129.0>-<702.0,132.0>>/L<<702.0,132.0>--<705.0,127.0>> = 2.726310993906212

	* petapp.minimal (U+E007): B<<723.5,10.0>-<723.0,5.0>-<722.0,0.0>>/B<<722.0,0.0>-<722.0,7.0>-<720.0,16.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<233.0,500.0>--<233.0,744.0>>/B<<233.0,744.0>-<236.0,686.0>-<276.0,646.0>> = 2.9609361341637563

	* petapp.minimal (U+E007): L<<561.0,361.0>--<575.0,346.0>>/B<<575.0,346.0>-<572.0,350.0>-<568.5,353.5>> = 6.155168343273918

	* petapp.minimal (U+E007): L<<664.0,258.0>--<667.0,254.0>>/B<<667.0,254.0>-<665.0,256.0>-<664.0,258.0>> = 8.13010235415596

	* petapp.minimal (U+E007): L<<679.0,240.0>--<680.0,237.0>>/B<<680.0,237.0>-<679.0,239.0>-<679.0,240.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<691.0,150.0>--<693.0,147.0>>/B<<693.0,147.0>-<692.0,148.0>-<691.0,150.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<694.0,218.0>--<695.0,215.0>>/B<<695.0,215.0>-<694.0,217.0>-<694.0,218.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<701.0,204.0>--<703.0,201.0>>/B<<703.0,201.0>-<702.0,203.0>-<701.0,204.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<702.0,132.0>--<705.0,127.0>>/B<<705.0,127.0>-<704.0,129.0>-<702.0,132.0>> = 4.398705354995508

	* petapp.minimal (U+E007): L<<721.0,84.0>--<722.0,81.0>>/B<<722.0,81.0>-<721.0,83.0>-<721.0,84.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<722.0,79.0>--<723.0,76.0>>/B<<723.0,76.0>-<722.0,78.0>-<722.0,79.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<723.0,145.0>--<724.0,140.0>>/B<<724.0,140.0>-<724.0,143.0>-<723.0,145.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<729.0,59.0>--<726.0,28.0>>/B<<726.0,28.0>-<726.0,29.0>-<726.0,29.0>> = 5.527540151656126

	* petapp.minimal (U+E007): L<<730.0,76.0>--<730.0,77.0>>/L<<730.0,77.0>--<729.0,69.0>> = 7.125016348901757

	* petapp.wpda (U+E008): B<<486.0,2.0>-<483.0,5.0>-<483.0,6.0>>/L<<483.0,6.0>--<482.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<207.0,206.0>--<202.0,203.0>>/B<<202.0,203.0>-<204.0,204.0>-<205.0,203.0>> = 4.398705354995426

	* pisafe (U+E010): B<<197.0,501.0>-<197.0,499.0>-<196.0,497.0>>/L<<196.0,497.0>--<197.0,501.0>> = 12.528807709151492

	* pisafe (U+E010): B<<215.0,540.0>-<215.0,539.0>-<214.0,537.0>>/L<<214.0,537.0>--<215.0,540.0>> = 8.13010235415587

	* pisafe (U+E010): B<<230.0,559.0>-<229.0,558.0>-<228.0,556.0>>/L<<228.0,556.0>--<230.0,559.0>> = 7.125016348901757

	* pisafe (U+E010): B<<246.0,573.0>-<244.0,572.0>-<243.0,571.0>>/L<<243.0,571.0>--<246.0,573.0>> = 11.309932474020227

	* pisafe (U+E010): B<<764.0,552.0>-<763.0,554.0>-<762.0,555.0>>/L<<762.0,555.0>--<764.0,552.0>> = 11.309932474020195

	* pisafe (U+E010): B<<776.0,535.0>-<776.0,536.0>-<775.0,538.0>>/L<<775.0,538.0>--<776.0,535.0>> = 8.13010235415587

	* pisafe (U+E010): B<<784.0,521.0>-<784.0,522.0>-<783.0,524.0>>/L<<783.0,524.0>--<784.0,521.0>> = 8.13010235415587

	* pisafe (U+E010): L<<196.0,497.0>--<197.0,501.0>>/B<<197.0,501.0>-<197.0,499.0>-<196.0,497.0>> = 14.036243467926484

	* pisafe (U+E010): L<<209.0,528.0>--<210.0,531.0>>/B<<210.0,531.0>-<209.0,529.0>-<209.0,528.0>> = 8.13010235415587

	* pisafe (U+E010): L<<228.0,556.0>--<230.0,559.0>>/B<<230.0,559.0>-<229.0,558.0>-<228.0,556.0>> = 11.309932474020195

	* pisafe (U+E010): L<<243.0,571.0>--<246.0,573.0>>/B<<246.0,573.0>-<244.0,572.0>-<243.0,571.0>> = 7.125016348901757

	* pisafe (U+E010): L<<732.0,582.0>--<735.0,580.0>>/B<<735.0,580.0>-<734.0,581.0>-<732.0,582.0>> = 11.309932474020227

	* pisafe (U+E010): L<<762.0,555.0>--<764.0,552.0>>/B<<764.0,552.0>-<763.0,554.0>-<762.0,555.0>> = 7.125016348901757

	* pisafe (U+E010): L<<793.0,497.0>--<794.0,492.0>>/B<<794.0,492.0>-<794.0,495.0>-<793.0,497.0>> = 11.309932474020195

	* pisafe (U+E010): L<<795.0,490.0>--<796.0,487.0>>/B<<796.0,487.0>-<795.0,489.0>-<795.0,490.0>> = 8.13010235415587 

	* pisafe (U+E010): L<<796.0,485.0>--<797.0,482.0>>/B<<797.0,482.0>-<796.0,484.0>-<796.0,485.0>> = 8.13010235415587 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* a (U+0061): L<<506.0,344.0>--<505.0,105.0>>

	* aacute (U+00E1): L<<506.0,344.0>--<505.0,105.0>>

	* abreve (U+0103): L<<506.0,344.0>--<505.0,105.0>>

	* acircumflex (U+00E2): L<<506.0,344.0>--<505.0,105.0>>

	* adieresis (U+00E4): L<<506.0,344.0>--<505.0,105.0>>

	* agrave (U+00E0): L<<506.0,344.0>--<505.0,105.0>>

	* amacron (U+0101): L<<506.0,344.0>--<505.0,105.0>>

	* aogonek (U+0105): L<<506.0,344.0>--<505.0,105.0>>

	* aring (U+00E5): L<<506.0,344.0>--<505.0,105.0>>

	* aringacute (U+01FB): L<<506.0,344.0>--<505.0,105.0>>

	* atilde (U+00E3): L<<506.0,344.0>--<505.0,105.0>>

	* dotlessi (U+0131): L<<215.0,472.0>--<216.0,27.0>>

	* fi (U+FB01): L<<606.0,472.0>--<607.0,27.0>>

	* h (U+0068): L<<216.0,373.0>--<214.0,27.0>>

	* hbar (U+0127): L<<216.0,373.0>--<214.0,27.0>>

	* hcircumflex (U+0125): L<<216.0,373.0>--<214.0,27.0>>

	* i (U+0069): L<<218.0,472.0>--<219.0,27.0>>

	* ibreve (U+012D): L<<215.0,472.0>--<216.0,27.0>>

	* ij (U+0133): L<<218.0,472.0>--<219.0,27.0>>

	* ij (U+0133): L<<521.0,479.0>--<523.0,-4.0>>

	* iogonek (U+012F): L<<218.0,472.0>--<219.0,27.0>>

	* itilde (U+0129): L<<215.0,472.0>--<216.0,27.0>>

	* j (U+006A): L<<235.0,479.0>--<237.0,-4.0>>

	* k (U+006B): L<<216.0,670.0>--<215.0,319.0>>

	* uni01C8 (U+01C8): L<<790.0,479.0>--<792.0,-4.0>>

	* uni01C9 (U+01C9): L<<515.0,479.0>--<517.0,-4.0>>

	* uni01CB (U+01CB): L<<959.0,479.0>--<961.0,-4.0>>

	* uni01CC (U+01CC): L<<844.0,479.0>--<846.0,-4.0>>

	* uni01CE (U+01CE): L<<506.0,344.0>--<505.0,105.0>>

	* uni01D0 (U+01D0): L<<215.0,472.0>--<216.0,27.0>>

	* uni0201 (U+0201): L<<506.0,344.0>--<505.0,105.0>>

	* uni0203 (U+0203): L<<506.0,344.0>--<505.0,105.0>>

	* uni0209 (U+0209): L<<215.0,472.0>--<216.0,27.0>>

	* uni020B (U+020B): L<<215.0,472.0>--<216.0,27.0>>

	* uni1E2B (U+1E2B): L<<216.0,373.0>--<214.0,27.0>>

	* uni1E2F (U+1E2F): L<<215.0,472.0>--<216.0,27.0>>

	* uni1E9E (U+1E9E): L<<232.0,425.0>--<231.0,27.0>>

	* uni1EA1 (U+1EA1): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EA3 (U+1EA3): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EA5 (U+1EA5): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EA7 (U+1EA7): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EA9 (U+1EA9): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EAB (U+1EAB): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EAD (U+1EAD): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EAF (U+1EAF): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EB1 (U+1EB1): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EB3 (U+1EB3): L<<506.0,344.0>--<505.0,105.0>>

	* uni1EB5 (U+1EB5): L<<506.0,344.0>--<505.0,105.0>> 

	* uni1EB7 (U+1EB7): L<<506.0,344.0>--<505.0,105.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[22] PitagonSans-ExtraBold.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Familyname must be unique according to namecheck.fontdata.com (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck">com.google.fonts/check/fontdata_namecheck</a>)</summary><div>


* 💔 **ERROR** Failed to access: http://namecheck.fontdata.com.
		This check relies on the external service http://namecheck.fontdata.com via the internet. While the service cannot be reached or does not respond this check is broken.

		You can exclude this check with the command line option:
		-x com.google.fonts/check/fontdata_namecheck

		Or you can wait until the service is available again.
		If the problem persists please report this issue at: https://github.com/googlefonts/fontbakery/issues

		Original error message:
		<class 'requests.exceptions.ConnectionError'> [code: namecheck-service]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x021A (LATIN CAPITAL LETTER T WITH COMMA BELOW)
 

	- 0x0312 (COMBINING TURNED COMMA ABOVE)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry TRADEMARK on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1175 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ i̛̇ i̛̊ i̛̋ i̤̇ i̤̊ i̤̋ i̦̇ i̦̊ i̦̋ i̧̇ i̧̊ i̧̋ i̮̇ i̮̊ i̮̋ i̱̇ i̱̊ i̱̋ i̵̇ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>


* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Pitagon Sans ExtraBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- caronalt

	- dotbelowcomb.case

	- hookabovecomb.case

	- ijacute

	- uni03020309

	- uni03060309

	- uni031B.case 

	- uni0326.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 578 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 551:
plus

Width = 667:
less

Width = 638:
equal

Width = 658:
greater

Width = 633:
logicalnot

Width = 585:
plusminus

Width = 526:
multiply

Width = 628:
divide

Width = 580:
minus

Width = 632:
approxequal

Width = 611:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* petapp (U+E006): L<<297.0,283.0>--<325.0,266.0>> -> L<<325.0,266.0>--<350.0,252.0>>

	* petapp (U+E006): L<<325.0,310.0>--<289.0,331.0>> -> L<<289.0,331.0>--<274.0,339.0>>

	* petapp (U+E006): L<<365.0,287.0>--<325.0,310.0>> -> L<<325.0,310.0>--<289.0,331.0>>

	* petapp (U+E006): L<<374.0,598.0>--<380.0,595.0>> -> L<<380.0,595.0>--<469.0,544.0>>

	* petapp (U+E006): L<<380.0,278.0>--<365.0,287.0>> -> L<<365.0,287.0>--<325.0,310.0>>

	* petapp (U+E006): L<<380.0,595.0>--<469.0,544.0>> -> L<<469.0,544.0>--<514.0,517.0>>

	* petapp (U+E006): L<<382.0,277.0>--<380.0,278.0>> -> L<<380.0,278.0>--<365.0,287.0>>

	* petapp (U+E006): L<<431.0,249.0>--<382.0,277.0>> -> L<<382.0,277.0>--<380.0,278.0>>

	* petapp (U+E006): L<<469.0,544.0>--<514.0,517.0>> -> L<<514.0,517.0>--<532.0,507.0>>

	* petapp (U+E006): L<<470.0,226.0>--<431.0,249.0>> -> L<<431.0,249.0>--<382.0,277.0>>

	* petapp (U+E006): L<<476.0,223.0>--<470.0,226.0>> -> L<<470.0,226.0>--<431.0,249.0>>

	* petapp (U+E006): L<<498.0,210.0>--<476.0,223.0>> -> L<<476.0,223.0>--<470.0,226.0>>

	* petapp (U+E006): L<<505.0,206.0>--<498.0,210.0>> -> L<<498.0,210.0>--<476.0,223.0>>

	* petapp (U+E006): L<<589.0,424.0>--<589.0,429.0>> -> L<<589.0,429.0>--<589.0,434.0>>

	* petapp (U+E006): L<<589.0,429.0>--<589.0,425.0>> -> L<<589.0,425.0>--<589.0,424.0>>

	* petapp (U+E006): L<<590.0,451.0>--<593.0,472.0>> -> L<<593.0,472.0>--<596.0,487.0>>

	* petapp (U+E006): L<<706.0,451.0>--<709.0,451.0>> -> L<<709.0,451.0>--<746.0,451.0>>

	* petapp.minimal (U+E007): L<<279.0,643.0>--<504.0,418.0>> -> L<<504.0,418.0>--<510.0,411.0>>

	* petapp.minimal (U+E007): L<<281.0,347.0>--<361.0,315.0>> -> L<<361.0,315.0>--<436.0,284.0>>

	* petapp.minimal (U+E007): L<<361.0,315.0>--<436.0,284.0>> -> L<<436.0,284.0>--<451.0,278.0>>

	* petapp.minimal (U+E007): L<<389.0,327.0>--<343.0,350.0>> -> L<<343.0,350.0>--<318.0,363.0>>

	* petapp.minimal (U+E007): L<<436.0,284.0>--<451.0,278.0>> -> L<<451.0,278.0>--<504.0,257.0>>

	* petapp.minimal (U+E007): L<<437.0,303.0>--<389.0,327.0>> -> L<<389.0,327.0>--<343.0,350.0>>

	* petapp.minimal (U+E007): L<<439.0,174.0>--<412.0,179.0>> -> L<<412.0,179.0>--<317.0,196.0>>

	* petapp.minimal (U+E007): L<<451.0,278.0>--<504.0,257.0>> -> L<<504.0,257.0>--<605.0,216.0>>

	* petapp.minimal (U+E007): L<<459.0,292.0>--<437.0,303.0>> -> L<<437.0,303.0>--<389.0,327.0>>

	* petapp.minimal (U+E007): L<<504.0,163.0>--<439.0,174.0>> -> L<<439.0,174.0>--<412.0,179.0>>

	* petapp.minimal (U+E007): L<<504.0,257.0>--<605.0,216.0>> -> L<<605.0,216.0>--<613.0,213.0>>

	* petapp.minimal (U+E007): L<<504.0,269.0>--<459.0,292.0>> -> L<<459.0,292.0>--<437.0,303.0>>

	* petapp.minimal (U+E007): L<<510.0,411.0>--<517.0,405.0>> -> L<<517.0,405.0>--<561.0,361.0>>

	* petapp.minimal (U+E007): L<<517.0,405.0>--<561.0,361.0>> -> L<<561.0,361.0>--<575.0,346.0>>

	* petapp.minimal (U+E007): L<<582.0,149.0>--<504.0,163.0>> -> L<<504.0,163.0>--<439.0,174.0>>

	* petapp.minimal (U+E007): L<<613.0,213.0>--<504.0,269.0>> -> L<<504.0,269.0>--<459.0,292.0>>

	* petapp.minimal (U+E007): L<<729.0,68.0>--<729.0,59.0>> -> L<<729.0,59.0>--<726.0,28.0>>

	* petapp.minimal (U+E007): L<<729.0,69.0>--<729.0,68.0>> -> L<<729.0,68.0>--<729.0,59.0>>

	* petapp.minimal (U+E007): L<<729.0,69.0>--<729.0,71.0>> -> L<<729.0,71.0>--<729.0,72.0>>

	* petapp.minimal (U+E007): L<<730.0,73.0>--<730.0,74.0>> -> L<<730.0,74.0>--<730.0,76.0>>

	* petapp.minimal (U+E007): L<<730.0,74.0>--<730.0,76.0>> -> L<<730.0,76.0>--<730.0,77.0>>

	* petapp.minimal (U+E007): L<<730.0,76.0>--<730.0,77.0>> -> L<<730.0,77.0>--<730.0,78.0>>

	* petapp.minimal (U+E007): L<<737.0,151.0>--<734.0,122.0>> -> L<<734.0,122.0>--<730.0,78.0>>

	* petapp.minimal (U+E007): L<<738.0,163.0>--<737.0,151.0>> -> L<<737.0,151.0>--<734.0,122.0>>

	* petapp.minimal (U+E007): L<<739.0,182.0>--<738.0,163.0>> -> L<<738.0,163.0>--<737.0,151.0>>

	* petapp.minimal (U+E007): L<<740.0,195.0>--<739.0,182.0>> -> L<<739.0,182.0>--<738.0,163.0>>

	* petapp.wpda (U+E008): L<<601.0,115.0>--<589.0,110.0>> -> L<<589.0,110.0>--<578.0,106.0>>

	* petapp.wpda (U+E008): L<<609.0,118.0>--<601.0,115.0>> -> L<<601.0,115.0>--<589.0,110.0>>

	* petapp.wpda (U+E008): L<<630.0,130.0>--<618.0,123.0>> -> L<<618.0,123.0>--<609.0,118.0>>

	* piads (U+E001): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* piads (U+E001): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* picall (U+E009): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* picall (U+E009): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* pioffice (U+E002): L<<138.0,503.0>--<142.0,506.0>> -> L<<142.0,506.0>--<447.0,728.0>>

	* pisafe (U+E010): L<<190.0,337.0>--<190.0,457.0>> -> L<<190.0,457.0>--<190.0,462.0>>

	* pisafe (U+E010): L<<218.0,644.0>--<223.0,646.0>> -> L<<223.0,646.0>--<257.0,658.0>>

	* pisafe (U+E010): L<<223.0,646.0>--<257.0,658.0>> -> L<<257.0,658.0>--<396.0,709.0>>

	* pisafe (U+E010): L<<257.0,658.0>--<396.0,709.0>> -> L<<396.0,709.0>--<494.0,744.0>>

	* pisafe (U+E010): L<<495.0,744.0>--<593.0,709.0>> -> L<<593.0,709.0>--<732.0,658.0>>

	* pisafe (U+E010): L<<593.0,709.0>--<732.0,658.0>> -> L<<732.0,658.0>--<766.0,646.0>>

	* pisafe (U+E010): L<<732.0,658.0>--<766.0,646.0>> -> L<<766.0,646.0>--<771.0,644.0>>

	* pisign (U+E005): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<851.0,505.0>>

	* pitagon (U+E000): L<<138.0,505.0>--<142.0,508.0>> -> L<<142.0,508.0>--<448.0,730.0>>

	* pitagon (U+E000): L<<229.0,57.0>--<112.0,415.0>> -> L<<112.0,415.0>--<110.0,420.0>>

	* pitagon (U+E000): L<<543.0,730.0>--<848.0,508.0>> -> L<<848.0,508.0>--<852.0,505.0>>

	* pitagram (U+E003): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>>

	* piweb (U+E004): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>>

	* sparks (U+E011): L<<130.0,741.0>--<219.0,709.0>> -> L<<219.0,709.0>--<229.0,706.0>>

	* sparks (U+E011): L<<219.0,709.0>--<229.0,706.0>> -> L<<229.0,706.0>--<407.0,642.0>>

	* sparks (U+E011): L<<229.0,706.0>--<407.0,642.0>> -> L<<407.0,642.0>--<435.0,632.0>>

	* sparks (U+E011): L<<305.0,554.0>--<372.0,497.0>> -> L<<372.0,497.0>--<390.0,480.0>>

	* sparks (U+E011): L<<389.0,340.0>--<391.0,341.0>> -> L<<391.0,341.0>--<487.0,399.0>>

	* sparks (U+E011): L<<415.0,95.0>--<126.0,596.0>> -> L<<126.0,596.0>--<78.0,680.0>>

	* sparks (U+E011): L<<424.0,589.0>--<383.0,585.0>> -> L<<383.0,585.0>--<363.0,583.0>>

	* sparks (U+E011): L<<444.0,613.0>--<440.0,604.0>> -> L<<440.0,604.0>--<438.0,598.0>>

	* sparks (U+E011): L<<457.0,22.0>--<415.0,95.0>> -> L<<415.0,95.0>--<126.0,596.0>>

	* sparks (U+E011): L<<503.0,399.0>--<598.0,341.0>> -> L<<598.0,341.0>--<600.0,340.0>>

	* sparks (U+E011): L<<554.0,632.0>--<589.0,645.0>> -> L<<589.0,645.0>--<760.0,706.0>>

	* sparks (U+E011): L<<573.0,94.0>--<546.0,47.0>> -> L<<546.0,47.0>--<532.0,22.0>>

	* sparks (U+E011): L<<589.0,645.0>--<760.0,706.0>> -> L<<760.0,706.0>--<785.0,714.0>>

	* sparks (U+E011): L<<599.0,480.0>--<618.0,497.0>> -> L<<618.0,497.0>--<685.0,554.0>>

	* sparks (U+E011): L<<606.0,585.0>--<571.0,588.0>> -> L<<571.0,588.0>--<563.0,589.0>>

	* sparks (U+E011): L<<644.0,582.0>--<606.0,585.0>> -> L<<606.0,585.0>--<571.0,588.0>>

	* sparks (U+E011): L<<645.0,582.0>--<644.0,582.0>> -> L<<644.0,582.0>--<606.0,585.0>>

	* sparks (U+E011): L<<676.0,579.0>--<645.0,582.0>> -> L<<645.0,582.0>--<644.0,582.0>>

	* sparks (U+E011): L<<677.0,579.0>--<676.0,579.0>> -> L<<676.0,579.0>--<645.0,582.0>>

	* sparks (U+E011): L<<732.0,369.0>--<573.0,94.0>> -> L<<573.0,94.0>--<546.0,47.0>>

	* sparks (U+E011): L<<760.0,706.0>--<785.0,714.0>> -> L<<785.0,714.0>--<859.0,741.0>>

	* sparks (U+E011): L<<869.0,606.0>--<732.0,369.0>> -> L<<732.0,369.0>--<573.0,94.0>>

	* sparks (U+E011): L<<911.0,679.0>--<869.0,606.0>> -> L<<869.0,606.0>--<732.0,369.0>> 

	* sparks (U+E011): L<<912.0,681.0>--<911.0,679.0>> -> L<<911.0,679.0>--<869.0,606.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<306.0,434.0>-<307.0,432.0>-<308.0,431.0>>/L<<308.0,431.0>--<306.0,434.0>> = 11.309932474020227

	* petapp (U+E006): B<<319.0,259.0>-<312.0,273.0>-<297.0,283.0>>/L<<297.0,283.0>--<325.0,266.0>> = 2.4263358316022132

	* petapp (U+E006): B<<327.0,409.0>-<328.0,408.0>-<330.0,407.0>>/L<<330.0,407.0>--<327.0,409.0>> = 7.125016348901757

	* petapp (U+E006): B<<340.0,399.0>-<341.0,398.0>-<343.0,397.0>>/L<<343.0,397.0>--<340.0,399.0>> = 7.125016348901757

	* petapp (U+E006): B<<492.0,62.0>-<494.0,62.0>-<496.0,63.0>>/L<<496.0,63.0>--<492.0,62.0>> = 12.528807709151463

	* petapp (U+E006): B<<518.0,61.0>-<519.0,61.0>-<521.0,62.0>>/L<<521.0,62.0>--<518.0,61.0>> = 8.130102354155916

	* petapp (U+E006): B<<528.0,63.0>-<526.0,63.0>-<524.0,62.0>>/L<<524.0,62.0>--<528.0,63.0>> = 12.528807709151492

	* petapp (U+E006): B<<532.0,92.0>-<533.0,94.0>-<535.0,96.0>>/L<<535.0,96.0>--<532.0,92.0>> = 8.130102354155916

	* petapp (U+E006): B<<534.0,178.0>-<533.0,179.0>-<532.0,181.0>>/L<<532.0,181.0>--<534.0,178.0>> = 7.125016348901757

	* petapp (U+E006): B<<534.0,64.0>-<532.0,64.0>-<530.0,63.0>>/L<<530.0,63.0>--<534.0,64.0>> = 12.528807709151492

	* petapp (U+E006): B<<535.0,286.0>-<534.0,287.0>-<532.0,288.0>>/L<<532.0,288.0>--<535.0,286.0>> = 7.125016348901757

	* petapp (U+E006): B<<536.0,100.0>-<537.0,101.0>-<538.0,103.0>>/L<<538.0,103.0>--<536.0,100.0>> = 7.125016348901705

	* petapp (U+E006): B<<537.0,407.0>-<536.0,408.0>-<534.0,409.0>>/L<<534.0,409.0>--<537.0,407.0>> = 7.125016348901757

	* petapp (U+E006): B<<569.0,252.0>-<568.0,254.0>-<567.0,255.0>>/L<<567.0,255.0>--<569.0,252.0>> = 11.309932474020195

	* petapp (U+E006): B<<592.0,394.0>-<592.0,396.0>-<591.0,398.0>>/L<<591.0,398.0>--<592.0,394.0>> = 12.528807709151492

	* petapp (U+E006): B<<602.0,357.0>-<603.0,355.0>-<603.0,353.0>>/L<<603.0,353.0>--<602.0,357.0>> = 14.036243467926484

	* petapp (U+E006): B<<612.0,331.0>-<613.0,329.0>-<614.0,328.0>>/L<<614.0,328.0>--<612.0,331.0>> = 11.309932474020227

	* petapp (U+E006): B<<615.0,326.0>-<615.0,325.0>-<616.0,323.0>>/L<<616.0,323.0>--<615.0,326.0>> = 8.130102354155916

	* petapp (U+E006): B<<634.0,295.0>-<635.0,294.0>-<636.0,292.0>>/L<<636.0,292.0>--<634.0,295.0>> = 7.125016348901705

	* petapp (U+E006): B<<645.0,371.0>-<645.0,370.0>-<646.0,368.0>>/L<<646.0,368.0>--<645.0,371.0>> = 8.130102354155916

	* petapp (U+E006): B<<648.0,410.0>-<648.0,409.0>-<647.0,407.0>>/L<<647.0,407.0>--<648.0,410.0>> = 8.13010235415587

	* petapp (U+E006): B<<657.0,294.0>-<658.0,293.0>-<660.0,292.0>>/L<<660.0,292.0>--<657.0,294.0>> = 7.125016348901757

	* petapp (U+E006): B<<657.0,424.0>-<656.0,422.0>-<655.0,421.0>>/L<<655.0,421.0>--<657.0,424.0>> = 11.309932474020195

	* petapp (U+E006): B<<667.0,139.0>-<668.0,141.0>-<669.0,142.0>>/L<<669.0,142.0>--<667.0,139.0>> = 11.309932474020227

	* petapp (U+E006): B<<669.0,251.0>-<668.0,253.0>-<667.0,254.0>>/L<<667.0,254.0>--<669.0,251.0>> = 11.309932474020195

	* petapp (U+E006): B<<689.0,274.0>-<690.0,274.0>-<692.0,273.0>>/L<<692.0,273.0>--<689.0,274.0>> = 8.130102354155916

	* petapp (U+E006): B<<698.0,450.0>-<697.0,450.0>-<695.0,449.0>>/L<<695.0,449.0>--<698.0,450.0>> = 8.13010235415587

	* petapp (U+E006): B<<726.0,26.0>-<725.0,26.0>-<723.0,27.0>>/L<<723.0,27.0>--<726.0,26.0>> = 8.13010235415587

	* petapp (U+E006): B<<744.0,6.0>-<743.0,7.0>-<742.0,9.0>>/L<<742.0,9.0>--<744.0,6.0>> = 7.125016348901757

	* petapp (U+E006): L<<308.0,431.0>--<306.0,434.0>>/B<<306.0,434.0>-<307.0,432.0>-<308.0,431.0>> = 7.125016348901705

	* petapp (U+E006): L<<330.0,407.0>--<327.0,409.0>>/B<<327.0,409.0>-<328.0,408.0>-<330.0,407.0>> = 11.309932474020195

	* petapp (U+E006): L<<343.0,397.0>--<340.0,399.0>>/B<<340.0,399.0>-<341.0,398.0>-<343.0,397.0>> = 11.309932474020195

	* petapp (U+E006): L<<392.0,107.0>--<391.0,110.0>>/B<<391.0,110.0>-<392.0,108.0>-<392.0,107.0>> = 8.130102354155916

	* petapp (U+E006): L<<429.0,67.0>--<426.0,68.0>>/B<<426.0,68.0>-<428.0,67.0>-<429.0,67.0>> = 8.130102354155916

	* petapp (U+E006): L<<459.0,57.0>--<456.0,58.0>>/B<<456.0,58.0>-<458.0,57.0>-<459.0,57.0>> = 8.130102354155916

	* petapp (U+E006): L<<489.0,61.0>--<486.0,60.0>>/B<<486.0,60.0>-<488.0,61.0>-<489.0,61.0>> = 8.130102354155916

	* petapp (U+E006): L<<496.0,63.0>--<492.0,62.0>>/B<<492.0,62.0>-<494.0,62.0>-<496.0,63.0>> = 14.036243467926484

	* petapp (U+E006): L<<499.0,209.0>--<505.0,206.0>>/L<<505.0,206.0>--<498.0,210.0>> = 3.1798301198640497

	* petapp (U+E006): L<<520.0,78.0>--<516.0,75.0>>/B<<516.0,75.0>-<518.0,76.0>-<520.0,78.0>> = 10.304846468766009

	* petapp (U+E006): L<<524.0,62.0>--<528.0,63.0>>/B<<528.0,63.0>-<526.0,63.0>-<524.0,62.0>> = 14.036243467926484

	* petapp (U+E006): L<<530.0,63.0>--<534.0,64.0>>/B<<534.0,64.0>-<532.0,64.0>-<530.0,63.0>> = 14.036243467926484

	* petapp (U+E006): L<<532.0,181.0>--<534.0,178.0>>/B<<534.0,178.0>-<533.0,179.0>-<532.0,181.0>> = 11.309932474020195

	* petapp (U+E006): L<<532.0,288.0>--<535.0,286.0>>/B<<535.0,286.0>-<534.0,287.0>-<532.0,288.0>> = 11.309932474020227

	* petapp (U+E006): L<<534.0,409.0>--<537.0,407.0>>/B<<537.0,407.0>-<536.0,408.0>-<534.0,409.0>> = 11.309932474020227

	* petapp (U+E006): L<<535.0,96.0>--<532.0,92.0>>/B<<532.0,92.0>-<533.0,94.0>-<535.0,96.0>> = 10.304846468765973

	* petapp (U+E006): L<<537.0,65.0>--<540.0,66.0>>/B<<540.0,66.0>-<538.0,65.0>-<537.0,65.0>> = 8.13010235415587

	* petapp (U+E006): L<<538.0,103.0>--<536.0,100.0>>/B<<536.0,100.0>-<537.0,101.0>-<538.0,103.0>> = 11.309932474020227

	* petapp (U+E006): L<<543.0,156.0>--<544.0,153.0>>/B<<544.0,153.0>-<543.0,155.0>-<543.0,156.0>> = 8.13010235415587

	* petapp (U+E006): L<<544.0,151.0>--<545.0,148.0>>/B<<545.0,148.0>-<544.0,150.0>-<544.0,151.0>> = 8.13010235415587

	* petapp (U+E006): L<<567.0,255.0>--<569.0,252.0>>/B<<569.0,252.0>-<568.0,254.0>-<567.0,255.0>> = 7.125016348901757

	* petapp (U+E006): L<<590.0,419.0>--<589.0,422.0>>/B<<589.0,422.0>-<590.0,420.0>-<590.0,419.0>> = 8.130102354155916

	* petapp (U+E006): L<<593.0,398.0>--<592.0,401.0>>/B<<592.0,401.0>-<593.0,399.0>-<593.0,397.5>> = 8.130102354155916

	* petapp (U+E006): L<<603.0,353.0>--<602.0,357.0>>/B<<602.0,357.0>-<603.0,355.0>-<603.0,353.0>> = 12.528807709151492

	* petapp (U+E006): L<<614.0,328.0>--<612.0,331.0>>/B<<612.0,331.0>-<613.0,329.0>-<614.0,328.0>> = 7.125016348901705

	* petapp (U+E006): L<<636.0,292.0>--<634.0,295.0>>/B<<634.0,295.0>-<635.0,294.0>-<636.0,292.0>> = 11.309932474020227

	* petapp (U+E006): L<<645.0,374.0>--<644.0,379.0>>/B<<644.0,379.0>-<644.0,376.0>-<645.0,374.0>> = 11.309932474020227

	* petapp (U+E006): L<<646.0,402.0>--<647.0,405.0>>/B<<647.0,405.0>-<646.0,403.0>-<645.5,402.0>> = 8.13010235415587

	* petapp (U+E006): L<<647.0,363.0>--<646.0,366.0>>/B<<646.0,366.0>-<647.0,364.0>-<647.0,363.0>> = 8.130102354155916

	* petapp (U+E006): L<<649.0,358.0>--<648.0,361.0>>/B<<648.0,361.0>-<649.0,359.0>-<649.0,358.0>> = 8.130102354155916

	* petapp (U+E006): L<<655.0,421.0>--<657.0,424.0>>/B<<657.0,424.0>-<656.0,422.0>-<655.0,421.0>> = 7.125016348901757

	* petapp (U+E006): L<<667.0,254.0>--<669.0,251.0>>/B<<669.0,251.0>-<668.0,253.0>-<667.0,254.0>> = 7.125016348901757

	* petapp (U+E006): L<<669.0,142.0>--<667.0,139.0>>/B<<667.0,139.0>-<668.0,141.0>-<669.0,142.0>> = 7.125016348901705

	* petapp (U+E006): L<<675.0,240.0>--<676.0,237.0>>/B<<676.0,237.0>-<675.0,239.0>-<675.0,240.0>> = 8.13010235415587

	* petapp (U+E006): L<<677.0,235.0>--<678.0,232.0>>/B<<678.0,232.0>-<677.0,234.0>-<677.0,235.0>> = 8.13010235415587

	* petapp (U+E006): L<<680.0,225.0>--<681.0,222.0>>/B<<681.0,222.0>-<680.0,224.0>-<680.0,225.0>> = 8.13010235415587

	* petapp (U+E006): L<<684.0,193.0>--<683.0,190.0>>/B<<683.0,190.0>-<684.0,192.0>-<684.0,193.0>> = 8.130102354155916

	* petapp (U+E006): L<<687.0,276.0>--<684.0,277.0>>/B<<684.0,277.0>-<686.0,276.0>-<687.0,276.0>> = 8.130102354155916

	* petapp (U+E006): L<<690.0,448.0>--<693.0,449.0>>/B<<693.0,449.0>-<691.0,448.0>-<690.0,448.0>> = 8.13010235415587

	* petapp (U+E006): L<<742.0,9.0>--<744.0,6.0>>/B<<744.0,6.0>-<743.0,7.0>-<742.0,9.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<627.0,385.0>-<628.0,383.0>-<629.0,382.0>>/L<<629.0,382.0>--<627.0,385.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<635.0,371.0>-<636.0,369.0>-<637.0,368.0>>/L<<637.0,368.0>--<635.0,371.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<636.0,202.0>-<635.0,202.0>-<633.0,203.0>>/L<<633.0,203.0>--<636.0,202.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<644.0,373.0>-<644.0,358.0>-<657.0,348.0>>/L<<657.0,348.0>--<653.0,351.0>> = 0.6986943829836932

	* petapp.minimal (U+E007): B<<667.0,254.0>-<666.0,256.0>-<664.0,258.0>>/L<<664.0,258.0>--<667.0,254.0>> = 8.13010235415596

	* petapp.minimal (U+E007): B<<671.0,504.0>-<670.0,504.0>-<668.0,503.0>>/L<<668.0,503.0>--<671.0,504.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<693.0,147.0>-<692.0,148.0>-<691.0,150.0>>/L<<691.0,150.0>--<693.0,147.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<695.0,215.0>-<694.0,217.0>-<693.0,218.0>>/L<<693.0,218.0>--<695.0,215.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<703.0,201.0>-<702.0,203.0>-<701.0,204.0>>/L<<701.0,204.0>--<703.0,201.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<705.0,127.0>-<704.0,129.0>-<702.0,132.0>>/L<<702.0,132.0>--<705.0,127.0>> = 2.726310993906212

	* petapp.minimal (U+E007): B<<723.5,10.0>-<723.0,5.0>-<722.0,0.0>>/B<<722.0,0.0>-<722.0,7.0>-<720.0,16.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<233.0,500.0>--<233.0,744.0>>/B<<233.0,744.0>-<236.0,686.0>-<276.0,646.0>> = 2.9609361341637563

	* petapp.minimal (U+E007): L<<561.0,361.0>--<575.0,346.0>>/B<<575.0,346.0>-<572.0,350.0>-<568.5,353.5>> = 6.155168343273918

	* petapp.minimal (U+E007): L<<623.0,397.0>--<622.0,400.0>>/B<<622.0,400.0>-<623.0,398.0>-<623.0,397.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<629.0,382.0>--<627.0,385.0>>/B<<627.0,385.0>-<628.0,383.0>-<629.0,382.0>> = 7.125016348901705

	* petapp.minimal (U+E007): L<<637.0,368.0>--<635.0,371.0>>/B<<635.0,371.0>-<636.0,369.0>-<637.0,368.0>> = 7.125016348901705

	* petapp.minimal (U+E007): L<<657.0,348.0>--<653.0,351.0>>/B<<653.0,351.0>-<655.0,350.0>-<657.0,348.0>> = 10.304846468766009

	* petapp.minimal (U+E007): L<<659.0,498.0>--<662.0,499.0>>/B<<662.0,499.0>-<660.0,498.0>-<659.0,498.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<664.0,258.0>--<667.0,254.0>>/B<<667.0,254.0>-<666.0,256.0>-<664.0,258.0>> = 10.304846468766044

	* petapp.minimal (U+E007): L<<679.0,240.0>--<680.0,237.0>>/B<<680.0,237.0>-<679.0,239.0>-<679.0,240.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<691.0,150.0>--<693.0,147.0>>/B<<693.0,147.0>-<692.0,148.0>-<691.0,150.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<693.0,218.0>--<695.0,215.0>>/B<<695.0,215.0>-<694.0,217.0>-<693.0,218.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<701.0,204.0>--<703.0,201.0>>/B<<703.0,201.0>-<702.0,203.0>-<701.0,204.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<702.0,132.0>--<705.0,127.0>>/B<<705.0,127.0>-<704.0,129.0>-<702.0,132.0>> = 4.398705354995508

	* petapp.minimal (U+E007): L<<721.0,84.0>--<722.0,81.0>>/B<<722.0,81.0>-<721.0,83.0>-<721.0,84.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<722.0,79.0>--<723.0,76.0>>/B<<723.0,76.0>-<722.0,78.0>-<722.0,79.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<723.0,145.0>--<724.0,140.0>>/B<<724.0,140.0>-<724.0,143.0>-<723.0,145.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<725.0,58.0>--<726.0,55.0>>/B<<726.0,55.0>-<725.0,57.0>-<725.0,58.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<729.0,59.0>--<726.0,28.0>>/B<<726.0,28.0>-<726.0,29.0>-<726.0,29.0>> = 5.527540151656126

	* petapp.wpda (U+E008): B<<486.0,2.0>-<483.0,5.0>-<483.0,6.0>>/L<<483.0,6.0>--<482.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<207.0,206.0>--<202.0,203.0>>/B<<202.0,203.0>-<204.0,204.0>-<205.0,203.0>> = 4.398705354995426

	* pisafe (U+E010): B<<197.0,501.0>-<197.0,499.0>-<196.0,497.0>>/L<<196.0,497.0>--<197.0,501.0>> = 12.528807709151492

	* pisafe (U+E010): B<<215.0,540.0>-<215.0,539.0>-<214.0,537.0>>/L<<214.0,537.0>--<215.0,540.0>> = 8.13010235415587

	* pisafe (U+E010): B<<230.0,559.0>-<229.0,558.0>-<228.0,556.0>>/L<<228.0,556.0>--<230.0,559.0>> = 7.125016348901757

	* pisafe (U+E010): B<<246.0,573.0>-<244.0,572.0>-<243.0,571.0>>/L<<243.0,571.0>--<246.0,573.0>> = 11.309932474020227

	* pisafe (U+E010): B<<764.0,552.0>-<763.0,554.0>-<762.0,555.0>>/L<<762.0,555.0>--<764.0,552.0>> = 11.309932474020195

	* pisafe (U+E010): B<<776.0,535.0>-<776.0,536.0>-<775.0,538.0>>/L<<775.0,538.0>--<776.0,535.0>> = 8.13010235415587

	* pisafe (U+E010): B<<784.0,521.0>-<784.0,522.0>-<783.0,524.0>>/L<<783.0,524.0>--<784.0,521.0>> = 8.13010235415587

	* pisafe (U+E010): L<<196.0,497.0>--<197.0,501.0>>/B<<197.0,501.0>-<197.0,499.0>-<196.0,497.0>> = 14.036243467926484

	* pisafe (U+E010): L<<209.0,528.0>--<210.0,531.0>>/B<<210.0,531.0>-<209.0,529.0>-<209.0,528.0>> = 8.13010235415587

	* pisafe (U+E010): L<<228.0,556.0>--<230.0,559.0>>/B<<230.0,559.0>-<229.0,558.0>-<228.0,556.0>> = 11.309932474020195

	* pisafe (U+E010): L<<243.0,571.0>--<246.0,573.0>>/B<<246.0,573.0>-<244.0,572.0>-<243.0,571.0>> = 7.125016348901757

	* pisafe (U+E010): L<<732.0,582.0>--<735.0,580.0>>/B<<735.0,580.0>-<734.0,581.0>-<732.0,582.0>> = 11.309932474020227

	* pisafe (U+E010): L<<762.0,555.0>--<764.0,552.0>>/B<<764.0,552.0>-<763.0,554.0>-<762.0,555.0>> = 7.125016348901757

	* pisafe (U+E010): L<<793.0,497.0>--<794.0,492.0>>/B<<794.0,492.0>-<794.0,495.0>-<793.0,497.0>> = 11.309932474020195

	* pisafe (U+E010): L<<795.0,490.0>--<796.0,487.0>>/B<<796.0,487.0>-<795.0,489.0>-<795.0,490.0>> = 8.13010235415587

	* pisafe (U+E010): L<<796.0,485.0>--<797.0,482.0>>/B<<797.0,482.0>-<796.0,484.0>-<796.0,485.0>> = 8.13010235415587 

	* section (U+00A7): B<<137.0,432.5>-<168.0,442.0>-<192.0,444.0>>/B<<192.0,444.0>-<181.0,445.0>-<165.0,457.0>> = 9.958070598460957 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* a (U+0061): L<<512.0,343.0>--<511.0,105.0>>

	* aacute (U+00E1): L<<512.0,343.0>--<511.0,105.0>>

	* abreve (U+0103): L<<512.0,343.0>--<511.0,105.0>>

	* acircumflex (U+00E2): L<<512.0,343.0>--<511.0,105.0>>

	* adieresis (U+00E4): L<<512.0,343.0>--<511.0,105.0>>

	* agrave (U+00E0): L<<512.0,343.0>--<511.0,105.0>>

	* amacron (U+0101): L<<512.0,343.0>--<511.0,105.0>>

	* aogonek (U+0105): L<<512.0,343.0>--<511.0,105.0>>

	* aring (U+00E5): L<<512.0,343.0>--<511.0,105.0>>

	* aringacute (U+01FB): L<<512.0,343.0>--<511.0,105.0>>

	* atilde (U+00E3): L<<512.0,343.0>--<511.0,105.0>>

	* dotlessi (U+0131): L<<229.0,469.0>--<230.0,30.0>>

	* fi (U+FB01): L<<626.0,469.0>--<628.0,30.0>>

	* h (U+0068): L<<229.0,367.0>--<227.0,30.0>>

	* hbar (U+0127): L<<229.0,367.0>--<227.0,30.0>>

	* hcircumflex (U+0125): L<<229.0,367.0>--<227.0,30.0>>

	* i (U+0069): L<<231.0,469.0>--<233.0,30.0>>

	* ibreve (U+012D): L<<229.0,469.0>--<230.0,30.0>>

	* ij (U+0133): L<<231.0,469.0>--<233.0,30.0>>

	* ij (U+0133): L<<542.0,478.0>--<544.0,2.0>>

	* iogonek (U+012F): L<<231.0,469.0>--<232.0,30.0>>

	* itilde (U+0129): L<<229.0,469.0>--<230.0,30.0>>

	* j (U+006A): L<<246.0,478.0>--<248.0,2.0>>

	* k (U+006B): L<<229.0,669.0>--<228.0,321.0>>

	* uni01C8 (U+01C8): L<<807.0,478.0>--<809.0,2.0>>

	* uni01C9 (U+01C9): L<<536.0,478.0>--<538.0,2.0>>

	* uni01CB (U+01CB): L<<971.0,478.0>--<973.0,2.0>>

	* uni01CC (U+01CC): L<<863.0,478.0>--<865.0,2.0>>

	* uni01CE (U+01CE): L<<512.0,343.0>--<511.0,105.0>>

	* uni01D0 (U+01D0): L<<229.0,469.0>--<230.0,30.0>>

	* uni0201 (U+0201): L<<512.0,343.0>--<511.0,105.0>>

	* uni0203 (U+0203): L<<512.0,343.0>--<511.0,105.0>>

	* uni0209 (U+0209): L<<229.0,469.0>--<230.0,30.0>>

	* uni020B (U+020B): L<<229.0,469.0>--<230.0,30.0>>

	* uni1E2B (U+1E2B): L<<229.0,367.0>--<227.0,30.0>>

	* uni1E2F (U+1E2F): L<<229.0,469.0>--<230.0,30.0>>

	* uni1E9E (U+1E9E): L<<248.0,417.0>--<247.0,30.0>>

	* uni1EA1 (U+1EA1): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EA3 (U+1EA3): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EA5 (U+1EA5): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EA7 (U+1EA7): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EA9 (U+1EA9): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EAB (U+1EAB): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EAD (U+1EAD): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EAF (U+1EAF): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EB1 (U+1EB1): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EB3 (U+1EB3): L<<512.0,343.0>--<511.0,105.0>>

	* uni1EB5 (U+1EB5): L<<512.0,343.0>--<511.0,105.0>> 

	* uni1EB7 (U+1EB7): L<<512.0,343.0>--<511.0,105.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[20] PitagonSans-Regular.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Familyname must be unique according to namecheck.fontdata.com (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck">com.google.fonts/check/fontdata_namecheck</a>)</summary><div>


* 💔 **ERROR** Failed to access: http://namecheck.fontdata.com.
		This check relies on the external service http://namecheck.fontdata.com via the internet. While the service cannot be reached or does not respond this check is broken.

		You can exclude this check with the command line option:
		-x com.google.fonts/check/fontdata_namecheck

		Or you can wait until the service is available again.
		If the problem persists please report this issue at: https://github.com/googlefonts/fontbakery/issues

		Original error message:
		<class 'requests.exceptions.ConnectionError'> [code: namecheck-service]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x021A (LATIN CAPITAL LETTER T WITH COMMA BELOW)
 

	- 0x0312 (COMBINING TURNED COMMA ABOVE)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry TRADEMARK on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1175 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ i̛̇ i̛̊ i̛̋ i̤̇ i̤̊ i̤̋ i̦̇ i̦̊ i̦̋ i̧̇ i̧̊ i̧̋ i̮̇ i̮̊ i̮̋ i̱̇ i̱̊ i̱̋ i̵̇ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>


* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- caronalt

	- dotbelowcomb.case

	- hookabovecomb.case

	- ijacute

	- uni03020309

	- uni03060309

	- uni031B.case 

	- uni0326.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 611 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 551:
plus

Width = 660:
less

Width = 638:
equal

Width = 649:
greater

Width = 622:
logicalnot

Width = 585:
plusminus

Width = 481:
multiply

Width = 628:
divide

Width = 566:
minus

Width = 568:
lessequal, greaterequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Iogonek (U+012E): L<<85.0,13.0>--<85.0,16.0>> -> L<<85.0,16.0>--<85.0,651.0>>

	* iogonek (U+012F): L<<84.0,14.0>--<84.0,16.0>> -> L<<84.0,16.0>--<84.0,483.0>>

	* petapp (U+E006): L<<296.0,283.0>--<324.0,266.0>> -> L<<324.0,266.0>--<349.0,252.0>>

	* petapp (U+E006): L<<324.0,310.0>--<288.0,331.0>> -> L<<288.0,331.0>--<273.0,339.0>>

	* petapp (U+E006): L<<364.0,287.0>--<324.0,310.0>> -> L<<324.0,310.0>--<288.0,331.0>>

	* petapp (U+E006): L<<373.0,598.0>--<379.0,595.0>> -> L<<379.0,595.0>--<468.0,544.0>>

	* petapp (U+E006): L<<379.0,278.0>--<364.0,287.0>> -> L<<364.0,287.0>--<324.0,310.0>>

	* petapp (U+E006): L<<379.0,595.0>--<468.0,544.0>> -> L<<468.0,544.0>--<513.0,517.0>>

	* petapp (U+E006): L<<381.0,277.0>--<379.0,278.0>> -> L<<379.0,278.0>--<364.0,287.0>>

	* petapp (U+E006): L<<430.0,249.0>--<381.0,277.0>> -> L<<381.0,277.0>--<379.0,278.0>>

	* petapp (U+E006): L<<468.0,544.0>--<513.0,517.0>> -> L<<513.0,517.0>--<531.0,507.0>>

	* petapp (U+E006): L<<469.0,226.0>--<430.0,249.0>> -> L<<430.0,249.0>--<381.0,277.0>>

	* petapp (U+E006): L<<475.0,223.0>--<469.0,226.0>> -> L<<469.0,226.0>--<430.0,249.0>>

	* petapp (U+E006): L<<497.0,210.0>--<475.0,223.0>> -> L<<475.0,223.0>--<469.0,226.0>>

	* petapp (U+E006): L<<504.0,206.0>--<497.0,210.0>> -> L<<497.0,210.0>--<475.0,223.0>>

	* petapp (U+E006): L<<588.0,424.0>--<588.0,429.0>> -> L<<588.0,429.0>--<588.0,434.0>>

	* petapp (U+E006): L<<588.0,429.0>--<588.0,425.0>> -> L<<588.0,425.0>--<588.0,424.0>>

	* petapp (U+E006): L<<589.0,451.0>--<592.0,472.0>> -> L<<592.0,472.0>--<595.0,487.0>>

	* petapp (U+E006): L<<705.0,451.0>--<708.0,451.0>> -> L<<708.0,451.0>--<745.0,451.0>>

	* petapp.minimal (U+E007): L<<280.0,347.0>--<361.0,315.0>> -> L<<361.0,315.0>--<436.0,284.0>>

	* petapp.minimal (U+E007): L<<361.0,315.0>--<436.0,284.0>> -> L<<436.0,284.0>--<451.0,278.0>>

	* petapp.minimal (U+E007): L<<389.0,327.0>--<342.0,350.0>> -> L<<342.0,350.0>--<318.0,363.0>>

	* petapp.minimal (U+E007): L<<436.0,284.0>--<451.0,278.0>> -> L<<451.0,278.0>--<503.0,257.0>>

	* petapp.minimal (U+E007): L<<436.0,303.0>--<389.0,327.0>> -> L<<389.0,327.0>--<342.0,350.0>>

	* petapp.minimal (U+E007): L<<439.0,174.0>--<411.0,179.0>> -> L<<411.0,179.0>--<317.0,196.0>>

	* petapp.minimal (U+E007): L<<451.0,278.0>--<503.0,257.0>> -> L<<503.0,257.0>--<604.0,216.0>>

	* petapp.minimal (U+E007): L<<458.0,292.0>--<436.0,303.0>> -> L<<436.0,303.0>--<389.0,327.0>>

	* petapp.minimal (U+E007): L<<503.0,163.0>--<439.0,174.0>> -> L<<439.0,174.0>--<411.0,179.0>>

	* petapp.minimal (U+E007): L<<503.0,257.0>--<604.0,216.0>> -> L<<604.0,216.0>--<612.0,213.0>>

	* petapp.minimal (U+E007): L<<503.0,269.0>--<458.0,292.0>> -> L<<458.0,292.0>--<436.0,303.0>>

	* petapp.minimal (U+E007): L<<581.0,149.0>--<503.0,163.0>> -> L<<503.0,163.0>--<439.0,174.0>>

	* petapp.minimal (U+E007): L<<612.0,213.0>--<503.0,269.0>> -> L<<503.0,269.0>--<458.0,292.0>>

	* petapp.minimal (U+E007): L<<725.0,28.0>--<725.0,29.0>> -> L<<725.0,29.0>--<725.0,30.0>>

	* petapp.minimal (U+E007): L<<726.0,31.0>--<726.0,32.0>> -> L<<726.0,32.0>--<726.0,33.0>>

	* petapp.minimal (U+E007): L<<726.0,32.0>--<726.0,33.0>> -> L<<726.0,33.0>--<726.0,34.0>>

	* petapp.minimal (U+E007): L<<726.0,33.0>--<726.0,34.0>> -> L<<726.0,34.0>--<726.0,35.0>>

	* petapp.minimal (U+E007): L<<726.0,34.0>--<726.0,35.0>> -> L<<726.0,35.0>--<726.0,36.0>>

	* petapp.minimal (U+E007): L<<726.0,35.0>--<726.0,36.0>> -> L<<726.0,36.0>--<726.0,37.0>>

	* petapp.minimal (U+E007): L<<726.0,36.0>--<726.0,37.0>> -> L<<726.0,37.0>--<726.0,38.0>>

	* petapp.minimal (U+E007): L<<726.0,38.0>--<725.0,28.0>> -> L<<725.0,28.0>--<725.0,20.0>>

	* petapp.minimal (U+E007): L<<729.0,68.0>--<728.0,59.0>> -> L<<728.0,59.0>--<726.0,38.0>>

	* petapp.minimal (U+E007): L<<734.0,122.0>--<729.0,69.0>> -> L<<729.0,69.0>--<729.0,68.0>>

	* petapp.minimal (U+E007): L<<736.0,151.0>--<734.0,122.0>> -> L<<734.0,122.0>--<729.0,69.0>>

	* petapp.minimal (U+E007): L<<737.0,163.0>--<736.0,151.0>> -> L<<736.0,151.0>--<734.0,122.0>>

	* petapp.minimal (U+E007): L<<739.0,182.0>--<737.0,163.0>> -> L<<737.0,163.0>--<736.0,151.0>>

	* petapp.minimal (U+E007): L<<740.0,195.0>--<739.0,182.0>> -> L<<739.0,182.0>--<737.0,163.0>>

	* petapp.minimal (U+E007): L<<740.0,198.0>--<740.0,195.0>> -> L<<740.0,195.0>--<739.0,182.0>>

	* petapp.wpda (U+E008): L<<601.0,115.0>--<589.0,110.0>> -> L<<589.0,110.0>--<578.0,106.0>>

	* petapp.wpda (U+E008): L<<609.0,118.0>--<601.0,115.0>> -> L<<601.0,115.0>--<589.0,110.0>>

	* petapp.wpda (U+E008): L<<630.0,130.0>--<618.0,123.0>> -> L<<618.0,123.0>--<609.0,118.0>>

	* piads (U+E001): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* piads (U+E001): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* picall (U+E009): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* picall (U+E009): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* pioffice (U+E002): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<851.0,505.0>>

	* pisafe (U+E010): L<<190.0,337.0>--<190.0,457.0>> -> L<<190.0,457.0>--<190.0,462.0>>

	* pisafe (U+E010): L<<218.0,644.0>--<223.0,646.0>> -> L<<223.0,646.0>--<257.0,658.0>>

	* pisafe (U+E010): L<<223.0,646.0>--<257.0,658.0>> -> L<<257.0,658.0>--<396.0,709.0>>

	* pisafe (U+E010): L<<257.0,658.0>--<396.0,709.0>> -> L<<396.0,709.0>--<494.0,744.0>>

	* pisafe (U+E010): L<<495.0,744.0>--<593.0,709.0>> -> L<<593.0,709.0>--<732.0,658.0>>

	* pisafe (U+E010): L<<593.0,709.0>--<732.0,658.0>> -> L<<732.0,658.0>--<766.0,646.0>>

	* pisafe (U+E010): L<<732.0,658.0>--<766.0,646.0>> -> L<<766.0,646.0>--<771.0,644.0>>

	* pisign (U+E005): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<851.0,505.0>>

	* pitagon (U+E000): L<<138.0,505.0>--<142.0,508.0>> -> L<<142.0,508.0>--<448.0,730.0>>

	* pitagon (U+E000): L<<229.0,57.0>--<112.0,415.0>> -> L<<112.0,415.0>--<110.0,420.0>>

	* pitagon (U+E000): L<<543.0,730.0>--<848.0,508.0>> -> L<<848.0,508.0>--<852.0,505.0>>

	* pitagram (U+E003): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>>

	* piweb (U+E004): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>>

	* sparks (U+E011): L<<130.0,741.0>--<219.0,709.0>> -> L<<219.0,709.0>--<229.0,706.0>>

	* sparks (U+E011): L<<219.0,709.0>--<229.0,706.0>> -> L<<229.0,706.0>--<407.0,642.0>>

	* sparks (U+E011): L<<229.0,706.0>--<407.0,642.0>> -> L<<407.0,642.0>--<435.0,632.0>>

	* sparks (U+E011): L<<305.0,554.0>--<372.0,497.0>> -> L<<372.0,497.0>--<390.0,480.0>>

	* sparks (U+E011): L<<389.0,340.0>--<391.0,341.0>> -> L<<391.0,341.0>--<487.0,399.0>>

	* sparks (U+E011): L<<415.0,95.0>--<126.0,596.0>> -> L<<126.0,596.0>--<78.0,680.0>>

	* sparks (U+E011): L<<424.0,589.0>--<383.0,585.0>> -> L<<383.0,585.0>--<363.0,583.0>>

	* sparks (U+E011): L<<444.0,613.0>--<440.0,604.0>> -> L<<440.0,604.0>--<438.0,598.0>>

	* sparks (U+E011): L<<457.0,22.0>--<415.0,95.0>> -> L<<415.0,95.0>--<126.0,596.0>>

	* sparks (U+E011): L<<503.0,399.0>--<598.0,341.0>> -> L<<598.0,341.0>--<600.0,340.0>>

	* sparks (U+E011): L<<554.0,632.0>--<589.0,645.0>> -> L<<589.0,645.0>--<760.0,706.0>>

	* sparks (U+E011): L<<573.0,94.0>--<546.0,47.0>> -> L<<546.0,47.0>--<532.0,22.0>>

	* sparks (U+E011): L<<589.0,645.0>--<760.0,706.0>> -> L<<760.0,706.0>--<785.0,714.0>>

	* sparks (U+E011): L<<599.0,480.0>--<618.0,497.0>> -> L<<618.0,497.0>--<685.0,554.0>>

	* sparks (U+E011): L<<606.0,585.0>--<571.0,588.0>> -> L<<571.0,588.0>--<563.0,589.0>>

	* sparks (U+E011): L<<644.0,582.0>--<606.0,585.0>> -> L<<606.0,585.0>--<571.0,588.0>>

	* sparks (U+E011): L<<645.0,582.0>--<644.0,582.0>> -> L<<644.0,582.0>--<606.0,585.0>>

	* sparks (U+E011): L<<676.0,579.0>--<645.0,582.0>> -> L<<645.0,582.0>--<644.0,582.0>>

	* sparks (U+E011): L<<677.0,579.0>--<676.0,579.0>> -> L<<676.0,579.0>--<645.0,582.0>>

	* sparks (U+E011): L<<732.0,369.0>--<573.0,94.0>> -> L<<573.0,94.0>--<546.0,47.0>>

	* sparks (U+E011): L<<760.0,706.0>--<785.0,714.0>> -> L<<785.0,714.0>--<859.0,741.0>>

	* sparks (U+E011): L<<869.0,606.0>--<732.0,369.0>> -> L<<732.0,369.0>--<573.0,94.0>>

	* sparks (U+E011): L<<911.0,679.0>--<869.0,606.0>> -> L<<869.0,606.0>--<732.0,369.0>> 

	* sparks (U+E011): L<<912.0,681.0>--<911.0,679.0>> -> L<<911.0,679.0>--<869.0,606.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<288.0,484.0>-<288.0,483.0>-<289.0,481.0>>/L<<289.0,481.0>--<288.0,484.0>> = 8.130102354155916

	* petapp (U+E006): B<<305.0,434.0>-<306.0,432.0>-<307.0,431.0>>/L<<307.0,431.0>--<305.0,434.0>> = 11.309932474020227

	* petapp (U+E006): B<<318.0,259.0>-<311.0,273.0>-<296.0,283.0>>/L<<296.0,283.0>--<324.0,266.0>> = 2.4263358316022132

	* petapp (U+E006): B<<326.0,409.0>-<328.0,408.0>-<329.0,407.0>>/L<<329.0,407.0>--<326.0,409.0>> = 11.309932474020195

	* petapp (U+E006): B<<339.0,399.0>-<340.0,398.0>-<342.0,397.0>>/L<<342.0,397.0>--<339.0,399.0>> = 7.125016348901757

	* petapp (U+E006): B<<430.0,65.0>-<431.0,65.0>-<433.0,64.0>>/L<<433.0,64.0>--<430.0,65.0>> = 8.130102354155916

	* petapp (U+E006): B<<435.0,63.0>-<436.0,63.0>-<438.0,62.0>>/L<<438.0,62.0>--<435.0,63.0>> = 8.130102354155916

	* petapp (U+E006): B<<440.0,61.0>-<441.0,61.0>-<443.0,60.0>>/L<<443.0,60.0>--<440.0,61.0>> = 8.130102354155916

	* petapp (U+E006): B<<491.0,62.0>-<493.0,62.0>-<495.0,63.0>>/L<<495.0,63.0>--<491.0,62.0>> = 12.528807709151463

	* petapp (U+E006): B<<517.0,61.0>-<518.0,61.0>-<520.0,62.0>>/L<<520.0,62.0>--<517.0,61.0>> = 8.130102354155916

	* petapp (U+E006): B<<531.0,92.0>-<532.0,94.0>-<534.0,96.0>>/L<<534.0,96.0>--<531.0,92.0>> = 8.130102354155916

	* petapp (U+E006): B<<533.0,178.0>-<532.0,179.0>-<531.0,181.0>>/L<<531.0,181.0>--<533.0,178.0>> = 7.125016348901757

	* petapp (U+E006): B<<533.0,64.0>-<531.0,64.0>-<529.0,63.0>>/L<<529.0,63.0>--<533.0,64.0>> = 12.528807709151492

	* petapp (U+E006): B<<534.0,286.0>-<533.0,287.0>-<531.0,288.0>>/L<<531.0,288.0>--<534.0,286.0>> = 7.125016348901757

	* petapp (U+E006): B<<536.0,100.0>-<536.0,101.0>-<537.0,103.0>>/L<<537.0,103.0>--<536.0,100.0>> = 8.130102354155916

	* petapp (U+E006): B<<568.0,252.0>-<567.0,254.0>-<566.0,255.0>>/L<<566.0,255.0>--<568.0,252.0>> = 11.309932474020195

	* petapp (U+E006): B<<592.0,123.0>-<592.0,122.0>-<593.0,120.0>>/L<<593.0,120.0>--<592.0,123.0>> = 8.130102354155916

	* petapp (U+E006): B<<601.0,357.0>-<602.0,355.0>-<602.0,353.0>>/L<<602.0,353.0>--<601.0,357.0>> = 14.036243467926484

	* petapp (U+E006): B<<626.0,324.0>-<627.0,323.0>-<628.0,321.0>>/L<<628.0,321.0>--<626.0,324.0>> = 7.125016348901705

	* petapp (U+E006): B<<633.0,295.0>-<634.0,294.0>-<635.0,292.0>>/L<<635.0,292.0>--<633.0,295.0>> = 7.125016348901705

	* petapp (U+E006): B<<644.0,371.0>-<644.0,370.0>-<645.0,368.0>>/L<<645.0,368.0>--<644.0,371.0>> = 8.130102354155916

	* petapp (U+E006): B<<649.0,356.0>-<650.0,355.0>-<651.0,353.0>>/L<<651.0,353.0>--<649.0,356.0>> = 7.125016348901705

	* petapp (U+E006): B<<656.0,294.0>-<658.0,293.0>-<659.0,292.0>>/L<<659.0,292.0>--<656.0,294.0>> = 11.309932474020195

	* petapp (U+E006): B<<656.0,424.0>-<655.0,422.0>-<654.0,421.0>>/L<<654.0,421.0>--<656.0,424.0>> = 11.309932474020195

	* petapp (U+E006): B<<666.0,132.0>-<667.0,132.0>-<669.0,133.0>>/L<<669.0,133.0>--<666.0,132.0>> = 8.130102354155916

	* petapp (U+E006): B<<666.0,139.0>-<667.0,141.0>-<668.0,142.0>>/L<<668.0,142.0>--<666.0,139.0>> = 11.309932474020227

	* petapp (U+E006): B<<668.0,251.0>-<667.0,253.0>-<666.0,254.0>>/L<<666.0,254.0>--<668.0,251.0>> = 11.309932474020195

	* petapp (U+E006): B<<678.0,56.0>-<680.0,54.0>-<682.0,53.0>>/L<<682.0,53.0>--<678.0,56.0>> = 10.304846468766009

	* petapp (U+E006): B<<681.0,178.0>-<681.0,180.0>-<682.0,182.0>>/L<<682.0,182.0>--<681.0,178.0>> = 12.528807709151492

	* petapp (U+E006): B<<693.0,272.0>-<694.0,272.0>-<696.0,271.0>>/L<<696.0,271.0>--<693.0,272.0>> = 8.130102354155916

	* petapp (U+E006): B<<743.0,6.0>-<742.0,7.0>-<741.0,9.0>>/L<<741.0,9.0>--<743.0,6.0>> = 7.125016348901757

	* petapp (U+E006): L<<307.0,431.0>--<305.0,434.0>>/B<<305.0,434.0>-<306.0,432.0>-<307.0,431.0>> = 7.125016348901705

	* petapp (U+E006): L<<329.0,407.0>--<326.0,409.0>>/B<<326.0,409.0>-<328.0,408.0>-<329.0,407.0>> = 7.125016348901757

	* petapp (U+E006): L<<342.0,397.0>--<339.0,399.0>>/B<<339.0,399.0>-<340.0,398.0>-<342.0,397.0>> = 11.309932474020195

	* petapp (U+E006): L<<391.0,107.0>--<390.0,110.0>>/B<<390.0,110.0>-<391.0,108.0>-<391.0,107.0>> = 8.130102354155916

	* petapp (U+E006): L<<453.0,58.0>--<450.0,59.0>>/B<<450.0,59.0>-<452.0,58.0>-<453.0,58.0>> = 8.130102354155916

	* petapp (U+E006): L<<495.0,63.0>--<491.0,62.0>>/B<<491.0,62.0>-<493.0,62.0>-<495.0,63.0>> = 14.036243467926484

	* petapp (U+E006): L<<498.0,209.0>--<504.0,206.0>>/L<<504.0,206.0>--<497.0,210.0>> = 3.1798301198640497

	* petapp (U+E006): L<<505.0,67.0>--<502.0,66.0>>/B<<502.0,66.0>-<504.0,67.0>-<505.0,67.0>> = 8.130102354155916

	* petapp (U+E006): L<<529.0,63.0>--<533.0,64.0>>/B<<533.0,64.0>-<531.0,64.0>-<529.0,63.0>> = 14.036243467926484

	* petapp (U+E006): L<<531.0,181.0>--<533.0,178.0>>/B<<533.0,178.0>-<532.0,179.0>-<531.0,181.0>> = 11.309932474020195

	* petapp (U+E006): L<<531.0,288.0>--<534.0,286.0>>/B<<534.0,286.0>-<533.0,287.0>-<531.0,288.0>> = 11.309932474020227

	* petapp (U+E006): L<<534.0,96.0>--<531.0,92.0>>/B<<531.0,92.0>-<532.0,94.0>-<534.0,96.0>> = 10.304846468765973

	* petapp (U+E006): L<<542.0,156.0>--<543.0,153.0>>/B<<543.0,153.0>-<542.0,155.0>-<542.0,156.0>> = 8.13010235415587

	* petapp (U+E006): L<<566.0,255.0>--<568.0,252.0>>/B<<568.0,252.0>-<567.0,254.0>-<566.0,255.0>> = 7.125016348901757

	* petapp (U+E006): L<<587.0,325.0>--<588.0,322.0>>/B<<588.0,322.0>-<587.0,324.0>-<587.0,325.0>> = 8.13010235415587

	* petapp (U+E006): L<<592.0,398.0>--<591.0,401.0>>/B<<591.0,401.0>-<592.0,399.0>-<592.0,397.5>> = 8.130102354155916

	* petapp (U+E006): L<<594.0,115.0>--<593.0,118.0>>/B<<593.0,118.0>-<594.0,116.0>-<594.0,114.5>> = 8.130102354155916

	* petapp (U+E006): L<<602.0,353.0>--<601.0,357.0>>/B<<601.0,357.0>-<602.0,355.0>-<602.0,353.0>> = 12.528807709151492

	* petapp (U+E006): L<<628.0,321.0>--<626.0,324.0>>/B<<626.0,324.0>-<627.0,323.0>-<628.0,321.0>> = 11.309932474020227

	* petapp (U+E006): L<<635.0,292.0>--<633.0,295.0>>/B<<633.0,295.0>-<634.0,294.0>-<635.0,292.0>> = 11.309932474020227

	* petapp (U+E006): L<<644.0,374.0>--<643.0,379.0>>/B<<643.0,379.0>-<643.0,376.0>-<644.0,374.0>> = 11.309932474020227

	* petapp (U+E006): L<<645.0,402.0>--<646.0,405.0>>/B<<646.0,405.0>-<645.0,403.0>-<645.0,402.0>> = 8.13010235415587

	* petapp (U+E006): L<<648.0,358.0>--<647.0,361.0>>/B<<647.0,361.0>-<648.0,359.0>-<648.0,358.0>> = 8.130102354155916

	* petapp (U+E006): L<<651.0,353.0>--<649.0,356.0>>/B<<649.0,356.0>-<650.0,355.0>-<651.0,353.0>> = 11.309932474020227

	* petapp (U+E006): L<<654.0,421.0>--<656.0,424.0>>/B<<656.0,424.0>-<655.0,422.0>-<654.0,421.0>> = 7.125016348901757

	* petapp (U+E006): L<<666.0,254.0>--<668.0,251.0>>/B<<668.0,251.0>-<667.0,253.0>-<666.0,254.0>> = 7.125016348901757

	* petapp (U+E006): L<<668.0,142.0>--<666.0,139.0>>/B<<666.0,139.0>-<667.0,141.0>-<668.0,142.0>> = 7.125016348901705

	* petapp (U+E006): L<<674.0,240.0>--<675.0,237.0>>/B<<675.0,237.0>-<674.0,239.0>-<674.0,240.0>> = 8.13010235415587

	* petapp (U+E006): L<<676.0,235.0>--<677.0,232.0>>/B<<677.0,232.0>-<676.0,234.0>-<676.0,235.0>> = 8.13010235415587

	* petapp (U+E006): L<<679.0,225.0>--<680.0,222.0>>/B<<680.0,222.0>-<679.0,224.0>-<679.0,225.0>> = 8.13010235415587

	* petapp (U+E006): L<<682.0,182.0>--<681.0,178.0>>/B<<681.0,178.0>-<681.0,180.0>-<682.0,182.0>> = 14.036243467926484

	* petapp (U+E006): L<<741.0,9.0>--<743.0,6.0>>/B<<743.0,6.0>-<742.0,7.0>-<741.0,9.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<640.0,199.0>-<639.0,199.0>-<637.0,200.0>>/L<<637.0,200.0>--<640.0,199.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<688.0,511.0>-<687.0,511.0>-<685.0,510.0>>/L<<685.0,510.0>--<688.0,511.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<692.0,147.0>-<692.0,148.0>-<691.0,150.0>>/L<<691.0,150.0>--<692.0,147.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<695.0,215.0>-<694.0,217.0>-<693.0,218.0>>/L<<693.0,218.0>--<695.0,215.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<703.0,201.0>-<702.0,203.0>-<701.0,204.0>>/L<<701.0,204.0>--<703.0,201.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<232.0,500.0>--<232.0,744.0>>/B<<232.0,744.0>-<235.0,686.0>-<275.0,646.0>> = 2.9609361341637563

	* petapp.minimal (U+E007): L<<622.0,400.0>--<621.0,405.0>>/B<<621.0,405.0>-<621.0,402.0>-<622.0,400.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<628.0,206.0>--<631.0,204.0>>/B<<631.0,204.0>-<629.0,205.0>-<628.0,206.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<680.0,509.0>--<683.0,510.0>>/B<<683.0,510.0>-<681.0,509.0>-<680.0,508.5>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<688.0,227.0>--<689.0,224.0>>/B<<689.0,224.0>-<688.0,226.0>-<688.0,227.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<693.0,218.0>--<695.0,215.0>>/B<<695.0,215.0>-<694.0,217.0>-<693.0,218.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<701.0,204.0>--<703.0,201.0>>/B<<703.0,201.0>-<702.0,203.0>-<701.0,204.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<711.0,114.0>--<712.0,111.0>>/B<<712.0,111.0>-<711.0,113.0>-<710.5,114.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<723.0,145.0>--<722.0,149.0>>/B<<722.0,149.0>-<723.0,143.0>-<723.0,145.0>> = 4.573921259900818

	* petapp.minimal (U+E007): L<<726.0,37.0>--<726.0,38.0>>/L<<726.0,38.0>--<725.0,28.0>> = 5.710593137499633

	* petapp.wpda (U+E008): B<<486.0,2.0>-<483.0,5.0>-<483.0,6.0>>/L<<483.0,6.0>--<482.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<207.0,206.0>--<202.0,203.0>>/B<<202.0,203.0>-<204.0,204.0>-<205.0,203.0>> = 4.398705354995426

	* pisafe (U+E010): B<<197.0,501.0>-<197.0,499.0>-<196.0,497.0>>/L<<196.0,497.0>--<197.0,501.0>> = 12.528807709151492

	* pisafe (U+E010): B<<215.0,540.0>-<215.0,539.0>-<214.0,537.0>>/L<<214.0,537.0>--<215.0,540.0>> = 8.13010235415587

	* pisafe (U+E010): B<<230.0,559.0>-<229.0,558.0>-<228.0,556.0>>/L<<228.0,556.0>--<230.0,559.0>> = 7.125016348901757

	* pisafe (U+E010): B<<246.0,573.0>-<244.0,572.0>-<243.0,571.0>>/L<<243.0,571.0>--<246.0,573.0>> = 11.309932474020227

	* pisafe (U+E010): B<<764.0,552.0>-<763.0,554.0>-<762.0,555.0>>/L<<762.0,555.0>--<764.0,552.0>> = 11.309932474020195

	* pisafe (U+E010): B<<776.0,535.0>-<776.0,536.0>-<775.0,538.0>>/L<<775.0,538.0>--<776.0,535.0>> = 8.13010235415587

	* pisafe (U+E010): B<<784.0,521.0>-<784.0,522.0>-<783.0,524.0>>/L<<783.0,524.0>--<784.0,521.0>> = 8.13010235415587

	* pisafe (U+E010): L<<196.0,497.0>--<197.0,501.0>>/B<<197.0,501.0>-<197.0,499.0>-<196.0,497.0>> = 14.036243467926484

	* pisafe (U+E010): L<<209.0,528.0>--<210.0,531.0>>/B<<210.0,531.0>-<209.0,529.0>-<209.0,528.0>> = 8.13010235415587

	* pisafe (U+E010): L<<228.0,556.0>--<230.0,559.0>>/B<<230.0,559.0>-<229.0,558.0>-<228.0,556.0>> = 11.309932474020195

	* pisafe (U+E010): L<<243.0,571.0>--<246.0,573.0>>/B<<246.0,573.0>-<244.0,572.0>-<243.0,571.0>> = 7.125016348901757

	* pisafe (U+E010): L<<732.0,582.0>--<735.0,580.0>>/B<<735.0,580.0>-<734.0,581.0>-<732.0,582.0>> = 11.309932474020227

	* pisafe (U+E010): L<<762.0,555.0>--<764.0,552.0>>/B<<764.0,552.0>-<763.0,554.0>-<762.0,555.0>> = 7.125016348901757

	* pisafe (U+E010): L<<793.0,497.0>--<794.0,492.0>>/B<<794.0,492.0>-<794.0,495.0>-<793.0,497.0>> = 11.309932474020195

	* pisafe (U+E010): L<<795.0,490.0>--<796.0,487.0>>/B<<796.0,487.0>-<795.0,489.0>-<795.0,490.0>> = 8.13010235415587 

	* pisafe (U+E010): L<<796.0,485.0>--<797.0,482.0>>/B<<797.0,482.0>-<796.0,484.0>-<796.0,485.0>> = 8.13010235415587 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[21] PitagonSans-Medium.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Familyname must be unique according to namecheck.fontdata.com (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck">com.google.fonts/check/fontdata_namecheck</a>)</summary><div>


* 💔 **ERROR** Failed to access: http://namecheck.fontdata.com.
		This check relies on the external service http://namecheck.fontdata.com via the internet. While the service cannot be reached or does not respond this check is broken.

		You can exclude this check with the command line option:
		-x com.google.fonts/check/fontdata_namecheck

		Or you can wait until the service is available again.
		If the problem persists please report this issue at: https://github.com/googlefonts/fontbakery/issues

		Original error message:
		<class 'requests.exceptions.ConnectionError'> [code: namecheck-service]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x021A (LATIN CAPITAL LETTER T WITH COMMA BELOW)
 

	- 0x0312 (COMBINING TURNED COMMA ABOVE)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry TRADEMARK on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1175 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ i̛̇ i̛̊ i̛̋ i̤̇ i̤̊ i̤̋ i̦̇ i̦̊ i̦̋ i̧̇ i̧̊ i̧̋ i̮̇ i̮̊ i̮̋ i̱̇ i̱̊ i̱̋ i̵̇ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>


* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- caronalt

	- dotbelowcomb.case

	- hookabovecomb.case

	- ijacute

	- uni03020309

	- uni03060309

	- uni031B.case 

	- uni0326.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 572 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 551:
plus

Width = 662:
less

Width = 638:
equal

Width = 652:
greater

Width = 626:
logicalnot

Width = 585:
plusminus

Width = 497:
multiply

Width = 628:
divide

Width = 571:
minus

Width = 619:
approxequal

Width = 611:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* petapp (U+E006): L<<296.0,283.0>--<324.0,266.0>> -> L<<324.0,266.0>--<349.0,252.0>>

	* petapp (U+E006): L<<324.0,310.0>--<288.0,331.0>> -> L<<288.0,331.0>--<273.0,339.0>>

	* petapp (U+E006): L<<364.0,287.0>--<324.0,310.0>> -> L<<324.0,310.0>--<288.0,331.0>>

	* petapp (U+E006): L<<373.0,598.0>--<379.0,595.0>> -> L<<379.0,595.0>--<468.0,544.0>>

	* petapp (U+E006): L<<379.0,278.0>--<364.0,287.0>> -> L<<364.0,287.0>--<324.0,310.0>>

	* petapp (U+E006): L<<379.0,595.0>--<468.0,544.0>> -> L<<468.0,544.0>--<513.0,517.0>>

	* petapp (U+E006): L<<381.0,277.0>--<379.0,278.0>> -> L<<379.0,278.0>--<364.0,287.0>>

	* petapp (U+E006): L<<430.0,249.0>--<381.0,277.0>> -> L<<381.0,277.0>--<379.0,278.0>>

	* petapp (U+E006): L<<468.0,544.0>--<513.0,517.0>> -> L<<513.0,517.0>--<531.0,507.0>>

	* petapp (U+E006): L<<469.0,226.0>--<430.0,249.0>> -> L<<430.0,249.0>--<381.0,277.0>>

	* petapp (U+E006): L<<475.0,223.0>--<469.0,226.0>> -> L<<469.0,226.0>--<430.0,249.0>>

	* petapp (U+E006): L<<497.0,210.0>--<475.0,223.0>> -> L<<475.0,223.0>--<469.0,226.0>>

	* petapp (U+E006): L<<504.0,206.0>--<497.0,210.0>> -> L<<497.0,210.0>--<475.0,223.0>>

	* petapp (U+E006): L<<589.0,451.0>--<592.0,472.0>> -> L<<592.0,472.0>--<595.0,487.0>>

	* petapp (U+E006): L<<705.0,451.0>--<708.0,451.0>> -> L<<708.0,451.0>--<745.0,451.0>>

	* petapp.minimal (U+E007): L<<278.0,643.0>--<503.0,418.0>> -> L<<503.0,418.0>--<510.0,411.0>>

	* petapp.minimal (U+E007): L<<280.0,347.0>--<361.0,315.0>> -> L<<361.0,315.0>--<436.0,284.0>>

	* petapp.minimal (U+E007): L<<361.0,315.0>--<436.0,284.0>> -> L<<436.0,284.0>--<451.0,278.0>>

	* petapp.minimal (U+E007): L<<389.0,327.0>--<342.0,350.0>> -> L<<342.0,350.0>--<318.0,363.0>>

	* petapp.minimal (U+E007): L<<436.0,284.0>--<451.0,278.0>> -> L<<451.0,278.0>--<503.0,257.0>>

	* petapp.minimal (U+E007): L<<436.0,303.0>--<389.0,327.0>> -> L<<389.0,327.0>--<342.0,350.0>>

	* petapp.minimal (U+E007): L<<439.0,174.0>--<411.0,179.0>> -> L<<411.0,179.0>--<317.0,196.0>>

	* petapp.minimal (U+E007): L<<451.0,278.0>--<503.0,257.0>> -> L<<503.0,257.0>--<604.0,216.0>>

	* petapp.minimal (U+E007): L<<458.0,292.0>--<436.0,303.0>> -> L<<436.0,303.0>--<389.0,327.0>>

	* petapp.minimal (U+E007): L<<503.0,163.0>--<439.0,174.0>> -> L<<439.0,174.0>--<411.0,179.0>>

	* petapp.minimal (U+E007): L<<503.0,257.0>--<604.0,216.0>> -> L<<604.0,216.0>--<612.0,213.0>>

	* petapp.minimal (U+E007): L<<503.0,269.0>--<458.0,292.0>> -> L<<458.0,292.0>--<436.0,303.0>>

	* petapp.minimal (U+E007): L<<503.0,418.0>--<510.0,411.0>> -> L<<510.0,411.0>--<516.0,405.0>>

	* petapp.minimal (U+E007): L<<510.0,411.0>--<516.0,405.0>> -> L<<516.0,405.0>--<560.0,361.0>>

	* petapp.minimal (U+E007): L<<516.0,405.0>--<560.0,361.0>> -> L<<560.0,361.0>--<575.0,346.0>>

	* petapp.minimal (U+E007): L<<581.0,149.0>--<503.0,163.0>> -> L<<503.0,163.0>--<439.0,174.0>>

	* petapp.minimal (U+E007): L<<613.0,213.0>--<503.0,269.0>> -> L<<503.0,269.0>--<458.0,292.0>>

	* petapp.minimal (U+E007): L<<726.0,30.0>--<726.0,31.0>> -> L<<726.0,31.0>--<726.0,32.0>>

	* petapp.minimal (U+E007): L<<726.0,31.0>--<726.0,32.0>> -> L<<726.0,32.0>--<726.0,33.0>>

	* petapp.minimal (U+E007): L<<726.0,32.0>--<726.0,33.0>> -> L<<726.0,33.0>--<726.0,34.0>>

	* petapp.minimal (U+E007): L<<726.0,34.0>--<726.0,34.0>> -> L<<726.0,34.0>--<726.0,34.0>>

	* petapp.minimal (U+E007): L<<729.0,68.0>--<728.0,59.0>> -> L<<728.0,59.0>--<726.0,34.0>>

	* petapp.minimal (U+E007): L<<734.0,122.0>--<729.0,69.0>> -> L<<729.0,69.0>--<729.0,68.0>>

	* petapp.minimal (U+E007): L<<736.0,151.0>--<734.0,122.0>> -> L<<734.0,122.0>--<729.0,69.0>>

	* petapp.minimal (U+E007): L<<737.0,163.0>--<736.0,151.0>> -> L<<736.0,151.0>--<734.0,122.0>>

	* petapp.minimal (U+E007): L<<739.0,182.0>--<737.0,163.0>> -> L<<737.0,163.0>--<736.0,151.0>>

	* petapp.minimal (U+E007): L<<740.0,195.0>--<739.0,182.0>> -> L<<739.0,182.0>--<737.0,163.0>>

	* petapp.minimal (U+E007): L<<740.0,198.0>--<740.0,195.0>> -> L<<740.0,195.0>--<739.0,182.0>>

	* petapp.wpda (U+E008): L<<601.0,115.0>--<589.0,110.0>> -> L<<589.0,110.0>--<578.0,106.0>>

	* petapp.wpda (U+E008): L<<609.0,118.0>--<601.0,115.0>> -> L<<601.0,115.0>--<589.0,110.0>>

	* petapp.wpda (U+E008): L<<630.0,130.0>--<618.0,123.0>> -> L<<618.0,123.0>--<609.0,118.0>>

	* piads (U+E001): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* piads (U+E001): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* picall (U+E009): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* picall (U+E009): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* pioffice (U+E002): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<447.0,729.0>>

	* pisafe (U+E010): L<<190.0,337.0>--<190.0,457.0>> -> L<<190.0,457.0>--<190.0,462.0>>

	* pisafe (U+E010): L<<218.0,644.0>--<223.0,646.0>> -> L<<223.0,646.0>--<257.0,658.0>>

	* pisafe (U+E010): L<<223.0,646.0>--<257.0,658.0>> -> L<<257.0,658.0>--<396.0,709.0>>

	* pisafe (U+E010): L<<257.0,658.0>--<396.0,709.0>> -> L<<396.0,709.0>--<494.0,744.0>>

	* pisafe (U+E010): L<<495.0,744.0>--<593.0,709.0>> -> L<<593.0,709.0>--<732.0,658.0>>

	* pisafe (U+E010): L<<593.0,709.0>--<732.0,658.0>> -> L<<732.0,658.0>--<766.0,646.0>>

	* pisafe (U+E010): L<<732.0,658.0>--<766.0,646.0>> -> L<<766.0,646.0>--<771.0,644.0>>

	* pisign (U+E005): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<851.0,505.0>>

	* pitagon (U+E000): L<<138.0,505.0>--<142.0,508.0>> -> L<<142.0,508.0>--<448.0,730.0>>

	* pitagon (U+E000): L<<229.0,57.0>--<112.0,415.0>> -> L<<112.0,415.0>--<110.0,420.0>>

	* pitagon (U+E000): L<<543.0,730.0>--<848.0,508.0>> -> L<<848.0,508.0>--<852.0,505.0>>

	* pitagram (U+E003): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>>

	* piweb (U+E004): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>>

	* sparks (U+E011): L<<130.0,741.0>--<219.0,709.0>> -> L<<219.0,709.0>--<229.0,706.0>>

	* sparks (U+E011): L<<219.0,709.0>--<229.0,706.0>> -> L<<229.0,706.0>--<407.0,642.0>>

	* sparks (U+E011): L<<229.0,706.0>--<407.0,642.0>> -> L<<407.0,642.0>--<435.0,632.0>>

	* sparks (U+E011): L<<305.0,554.0>--<372.0,497.0>> -> L<<372.0,497.0>--<390.0,480.0>>

	* sparks (U+E011): L<<389.0,340.0>--<391.0,341.0>> -> L<<391.0,341.0>--<487.0,399.0>>

	* sparks (U+E011): L<<415.0,95.0>--<126.0,596.0>> -> L<<126.0,596.0>--<78.0,680.0>>

	* sparks (U+E011): L<<424.0,589.0>--<383.0,585.0>> -> L<<383.0,585.0>--<363.0,583.0>>

	* sparks (U+E011): L<<444.0,613.0>--<440.0,604.0>> -> L<<440.0,604.0>--<438.0,598.0>>

	* sparks (U+E011): L<<457.0,22.0>--<415.0,95.0>> -> L<<415.0,95.0>--<126.0,596.0>>

	* sparks (U+E011): L<<503.0,399.0>--<598.0,341.0>> -> L<<598.0,341.0>--<600.0,340.0>>

	* sparks (U+E011): L<<554.0,632.0>--<589.0,645.0>> -> L<<589.0,645.0>--<760.0,706.0>>

	* sparks (U+E011): L<<573.0,94.0>--<546.0,47.0>> -> L<<546.0,47.0>--<532.0,22.0>>

	* sparks (U+E011): L<<589.0,645.0>--<760.0,706.0>> -> L<<760.0,706.0>--<785.0,714.0>>

	* sparks (U+E011): L<<599.0,480.0>--<618.0,497.0>> -> L<<618.0,497.0>--<685.0,554.0>>

	* sparks (U+E011): L<<606.0,585.0>--<571.0,588.0>> -> L<<571.0,588.0>--<563.0,589.0>>

	* sparks (U+E011): L<<644.0,582.0>--<606.0,585.0>> -> L<<606.0,585.0>--<571.0,588.0>>

	* sparks (U+E011): L<<645.0,582.0>--<644.0,582.0>> -> L<<644.0,582.0>--<606.0,585.0>>

	* sparks (U+E011): L<<676.0,579.0>--<645.0,582.0>> -> L<<645.0,582.0>--<644.0,582.0>>

	* sparks (U+E011): L<<677.0,579.0>--<676.0,579.0>> -> L<<676.0,579.0>--<645.0,582.0>>

	* sparks (U+E011): L<<732.0,369.0>--<573.0,94.0>> -> L<<573.0,94.0>--<546.0,47.0>>

	* sparks (U+E011): L<<760.0,706.0>--<785.0,714.0>> -> L<<785.0,714.0>--<859.0,741.0>>

	* sparks (U+E011): L<<869.0,606.0>--<732.0,369.0>> -> L<<732.0,369.0>--<573.0,94.0>>

	* sparks (U+E011): L<<911.0,679.0>--<869.0,606.0>> -> L<<869.0,606.0>--<732.0,369.0>> 

	* sparks (U+E011): L<<912.0,681.0>--<911.0,679.0>> -> L<<911.0,679.0>--<869.0,606.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<299.0,448.0>-<299.0,447.0>-<300.0,445.0>>/L<<300.0,445.0>--<299.0,448.0>> = 8.130102354155916

	* petapp (U+E006): B<<318.0,259.0>-<311.0,273.0>-<296.0,283.0>>/L<<296.0,283.0>--<324.0,266.0>> = 2.4263358316022132

	* petapp (U+E006): B<<339.0,399.0>-<341.0,398.0>-<342.0,397.0>>/L<<342.0,397.0>--<339.0,399.0>> = 11.309932474020195

	* petapp (U+E006): B<<491.0,62.0>-<493.0,62.0>-<495.0,63.0>>/L<<495.0,63.0>--<491.0,62.0>> = 12.528807709151463

	* petapp (U+E006): B<<511.0,60.0>-<513.0,60.0>-<515.0,61.0>>/L<<515.0,61.0>--<511.0,60.0>> = 12.528807709151463

	* petapp (U+E006): B<<517.0,61.0>-<518.0,61.0>-<521.0,62.0>>/L<<521.0,62.0>--<517.0,61.0>> = 4.398705354995508

	* petapp (U+E006): B<<527.0,63.0>-<526.0,63.0>-<524.0,62.0>>/L<<524.0,62.0>--<527.0,63.0>> = 8.13010235415587

	* petapp (U+E006): B<<531.0,92.0>-<533.0,94.0>-<534.0,96.0>>/L<<534.0,96.0>--<531.0,92.0>> = 10.304846468765973

	* petapp (U+E006): B<<533.0,178.0>-<532.0,179.0>-<531.0,181.0>>/L<<531.0,181.0>--<533.0,178.0>> = 7.125016348901757

	* petapp (U+E006): B<<534.0,286.0>-<533.0,287.0>-<531.0,288.0>>/L<<531.0,288.0>--<534.0,286.0>> = 7.125016348901757

	* petapp (U+E006): B<<591.0,128.0>-<591.0,127.0>-<592.0,125.0>>/L<<592.0,125.0>--<591.0,128.0>> = 8.130102354155916

	* petapp (U+E006): B<<591.0,401.0>-<591.0,402.0>-<590.0,404.0>>/L<<590.0,404.0>--<591.0,401.0>> = 8.13010235415587

	* petapp (U+E006): B<<592.0,123.0>-<592.0,122.0>-<593.0,120.0>>/L<<593.0,120.0>--<592.0,123.0>> = 8.130102354155916

	* petapp (U+E006): B<<611.0,346.0>-<612.0,345.0>-<613.0,343.0>>/L<<613.0,343.0>--<611.0,346.0>> = 7.125016348901705

	* petapp (U+E006): B<<626.0,324.0>-<627.0,323.0>-<628.0,321.0>>/L<<628.0,321.0>--<626.0,324.0>> = 7.125016348901705

	* petapp (U+E006): B<<634.0,295.0>-<634.0,294.0>-<635.0,292.0>>/L<<635.0,292.0>--<634.0,295.0>> = 8.130102354155916

	* petapp (U+E006): B<<643.0,379.0>-<644.0,376.0>-<644.0,374.0>>/L<<644.0,374.0>--<643.0,379.0>> = 11.309932474020227

	* petapp (U+E006): B<<650.0,356.0>-<650.0,355.0>-<651.0,353.0>>/L<<651.0,353.0>--<650.0,356.0>> = 8.130102354155916

	* petapp (U+E006): B<<656.0,294.0>-<658.0,293.0>-<659.0,292.0>>/L<<659.0,292.0>--<656.0,294.0>> = 11.309932474020195

	* petapp (U+E006): B<<656.0,424.0>-<655.0,422.0>-<654.0,421.0>>/L<<654.0,421.0>--<656.0,424.0>> = 11.309932474020195

	* petapp (U+E006): B<<678.0,56.0>-<680.0,54.0>-<682.0,53.0>>/L<<682.0,53.0>--<678.0,56.0>> = 10.304846468766009

	* petapp (U+E006): B<<681.0,178.0>-<682.0,180.0>-<682.0,182.0>>/L<<682.0,182.0>--<681.0,178.0>> = 14.036243467926484

	* petapp (U+E006): B<<682.0,445.0>-<680.0,444.0>-<679.0,443.0>>/L<<679.0,443.0>--<682.0,445.0>> = 11.309932474020227

	* petapp (U+E006): L<<342.0,397.0>--<339.0,399.0>>/B<<339.0,399.0>-<341.0,398.0>-<342.0,397.0>> = 7.125016348901757

	* petapp (U+E006): L<<387.0,128.0>--<386.0,131.0>>/B<<386.0,131.0>-<387.0,129.0>-<387.0,128.0>> = 8.130102354155916

	* petapp (U+E006): L<<390.0,112.0>--<389.0,115.0>>/B<<389.0,115.0>-<390.0,113.0>-<390.0,112.0>> = 8.130102354155916

	* petapp (U+E006): L<<448.0,59.0>--<445.0,60.0>>/B<<445.0,60.0>-<447.0,59.0>-<448.0,59.0>> = 8.130102354155916

	* petapp (U+E006): L<<495.0,63.0>--<491.0,62.0>>/B<<491.0,62.0>-<493.0,62.0>-<495.0,63.0>> = 14.036243467926484

	* petapp (U+E006): L<<498.0,209.0>--<504.0,206.0>>/L<<504.0,206.0>--<497.0,210.0>> = 3.1798301198640497

	* petapp (U+E006): L<<515.0,61.0>--<511.0,60.0>>/B<<511.0,60.0>-<513.0,60.0>-<515.0,61.0>> = 14.036243467926484

	* petapp (U+E006): L<<521.0,62.0>--<517.0,61.0>>/B<<517.0,61.0>-<518.0,61.0>-<521.0,62.0>> = 14.036243467926484

	* petapp (U+E006): L<<531.0,181.0>--<533.0,178.0>>/B<<533.0,178.0>-<532.0,179.0>-<531.0,181.0>> = 11.309932474020195

	* petapp (U+E006): L<<531.0,288.0>--<534.0,286.0>>/B<<534.0,286.0>-<533.0,287.0>-<531.0,288.0>> = 11.309932474020227

	* petapp (U+E006): L<<534.0,96.0>--<531.0,92.0>>/B<<531.0,92.0>-<533.0,94.0>-<534.0,96.0>> = 8.130102354155916

	* petapp (U+E006): L<<535.0,176.0>--<536.0,173.0>>/B<<536.0,173.0>-<535.0,175.0>-<535.0,176.0>> = 8.13010235415587

	* petapp (U+E006): L<<552.0,69.0>--<549.0,68.0>>/B<<549.0,68.0>-<551.0,69.0>-<552.0,69.0>> = 8.130102354155916

	* petapp (U+E006): L<<567.0,255.0>--<568.0,252.0>>/B<<568.0,252.0>-<567.0,254.0>-<567.0,255.0>> = 8.13010235415587

	* petapp (U+E006): L<<594.0,115.0>--<593.0,118.0>>/B<<593.0,118.0>-<594.0,116.0>-<594.0,114.5>> = 8.130102354155916

	* petapp (U+E006): L<<613.0,343.0>--<611.0,346.0>>/B<<611.0,346.0>-<612.0,345.0>-<613.0,343.0>> = 11.309932474020227

	* petapp (U+E006): L<<628.0,321.0>--<626.0,324.0>>/B<<626.0,324.0>-<627.0,323.0>-<628.0,321.0>> = 11.309932474020227

	* petapp (U+E006): L<<644.0,374.0>--<643.0,379.0>>/B<<643.0,379.0>-<644.0,376.0>-<644.0,374.0>> = 7.125016348901757

	* petapp (U+E006): L<<645.0,402.0>--<646.0,405.0>>/B<<646.0,405.0>-<645.0,403.0>-<645.0,402.0>> = 8.13010235415587

	* petapp (U+E006): L<<654.0,421.0>--<656.0,424.0>>/B<<656.0,424.0>-<655.0,422.0>-<654.0,421.0>> = 7.125016348901757

	* petapp (U+E006): L<<665.0,77.0>--<666.0,76.0>>/B<<666.0,76.0>-<664.0,79.0>-<665.0,77.0>> = 11.309932474020227

	* petapp (U+E006): L<<667.0,254.0>--<668.0,251.0>>/B<<668.0,251.0>-<667.0,253.0>-<667.0,254.0>> = 8.13010235415587

	* petapp (U+E006): L<<678.0,230.0>--<679.0,227.0>>/B<<679.0,227.0>-<678.0,229.0>-<678.0,230.0>> = 8.13010235415587

	* petapp (U+E006): L<<679.0,443.0>--<682.0,445.0>>/B<<682.0,445.0>-<680.0,444.0>-<679.0,443.0>> = 7.125016348901757

	* petapp (U+E006): L<<682.0,182.0>--<681.0,178.0>>/B<<681.0,178.0>-<682.0,180.0>-<682.0,182.0>> = 12.528807709151492

	* petapp (U+E006): L<<701.0,269.0>--<698.0,270.0>>/B<<698.0,270.0>-<700.0,269.0>-<701.0,269.0>> = 8.130102354155916

	* petapp (U+E006): L<<706.0,267.0>--<703.0,268.0>>/B<<703.0,268.0>-<705.0,267.0>-<706.0,267.0>> = 8.130102354155916

	* petapp (U+E006): L<<718.0,29.0>--<721.0,28.0>>/B<<721.0,28.0>-<719.0,29.0>-<718.0,29.5>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<621.0,440.0>-<621.0,439.0>-<620.0,437.0>>/L<<620.0,437.0>--<621.0,440.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<622.0,445.0>-<622.0,444.0>-<621.0,442.0>>/L<<621.0,442.0>--<622.0,445.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<640.0,199.0>-<639.0,199.0>-<637.0,200.0>>/L<<637.0,200.0>--<640.0,199.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<666.0,502.0>-<664.0,501.0>-<663.0,500.0>>/L<<663.0,500.0>--<666.0,502.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<676.0,507.0>-<674.0,506.0>-<673.0,505.0>>/L<<673.0,505.0>--<676.0,507.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<688.0,511.0>-<687.0,511.0>-<685.0,510.0>>/L<<685.0,510.0>--<688.0,511.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<692.0,147.0>-<692.0,148.0>-<691.0,150.0>>/L<<691.0,150.0>--<692.0,147.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<698.0,138.0>-<698.0,139.0>-<697.0,141.0>>/L<<697.0,141.0>--<698.0,138.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<703.0,201.0>-<702.0,203.0>-<701.0,204.0>>/L<<701.0,204.0>--<703.0,201.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<232.0,500.0>--<232.0,744.0>>/B<<232.0,744.0>-<235.0,686.0>-<275.0,646.0>> = 2.9609361341637563

	* petapp.minimal (U+E007): L<<622.0,400.0>--<621.0,405.0>>/B<<621.0,405.0>-<621.0,402.0>-<622.0,400.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<628.0,206.0>--<631.0,204.0>>/B<<631.0,204.0>-<629.0,205.0>-<628.0,206.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<663.0,500.0>--<666.0,502.0>>/B<<666.0,502.0>-<664.0,501.0>-<663.0,500.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<673.0,505.0>--<676.0,507.0>>/B<<676.0,507.0>-<674.0,506.0>-<673.0,505.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<679.0,240.0>--<680.0,237.0>>/B<<680.0,237.0>-<679.0,239.0>-<679.0,240.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<688.0,227.0>--<689.0,224.0>>/B<<689.0,224.0>-<688.0,226.0>-<688.0,227.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<694.0,218.0>--<695.0,215.0>>/B<<695.0,215.0>-<694.0,217.0>-<694.0,218.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<701.0,204.0>--<703.0,201.0>>/B<<703.0,201.0>-<702.0,203.0>-<701.0,204.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<711.0,114.0>--<712.0,111.0>>/B<<712.0,111.0>-<711.0,113.0>-<710.5,114.0>> = 8.13010235415587

	* petapp.wpda (U+E008): B<<486.0,2.0>-<483.0,5.0>-<483.0,6.0>>/L<<483.0,6.0>--<482.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<207.0,206.0>--<202.0,203.0>>/B<<202.0,203.0>-<204.0,204.0>-<205.0,203.0>> = 4.398705354995426

	* pisafe (U+E010): B<<197.0,501.0>-<197.0,499.0>-<196.0,497.0>>/L<<196.0,497.0>--<197.0,501.0>> = 12.528807709151492

	* pisafe (U+E010): B<<215.0,540.0>-<215.0,539.0>-<214.0,537.0>>/L<<214.0,537.0>--<215.0,540.0>> = 8.13010235415587

	* pisafe (U+E010): B<<230.0,559.0>-<229.0,558.0>-<228.0,556.0>>/L<<228.0,556.0>--<230.0,559.0>> = 7.125016348901757

	* pisafe (U+E010): B<<246.0,573.0>-<244.0,572.0>-<243.0,571.0>>/L<<243.0,571.0>--<246.0,573.0>> = 11.309932474020227

	* pisafe (U+E010): B<<764.0,552.0>-<763.0,554.0>-<762.0,555.0>>/L<<762.0,555.0>--<764.0,552.0>> = 11.309932474020195

	* pisafe (U+E010): B<<776.0,535.0>-<776.0,536.0>-<775.0,538.0>>/L<<775.0,538.0>--<776.0,535.0>> = 8.13010235415587

	* pisafe (U+E010): B<<784.0,521.0>-<784.0,522.0>-<783.0,524.0>>/L<<783.0,524.0>--<784.0,521.0>> = 8.13010235415587

	* pisafe (U+E010): L<<196.0,497.0>--<197.0,501.0>>/B<<197.0,501.0>-<197.0,499.0>-<196.0,497.0>> = 14.036243467926484

	* pisafe (U+E010): L<<209.0,528.0>--<210.0,531.0>>/B<<210.0,531.0>-<209.0,529.0>-<209.0,528.0>> = 8.13010235415587

	* pisafe (U+E010): L<<228.0,556.0>--<230.0,559.0>>/B<<230.0,559.0>-<229.0,558.0>-<228.0,556.0>> = 11.309932474020195

	* pisafe (U+E010): L<<243.0,571.0>--<246.0,573.0>>/B<<246.0,573.0>-<244.0,572.0>-<243.0,571.0>> = 7.125016348901757

	* pisafe (U+E010): L<<732.0,582.0>--<735.0,580.0>>/B<<735.0,580.0>-<734.0,581.0>-<732.0,582.0>> = 11.309932474020227

	* pisafe (U+E010): L<<762.0,555.0>--<764.0,552.0>>/B<<764.0,552.0>-<763.0,554.0>-<762.0,555.0>> = 7.125016348901757

	* pisafe (U+E010): L<<793.0,497.0>--<794.0,492.0>>/B<<794.0,492.0>-<794.0,495.0>-<793.0,497.0>> = 11.309932474020195

	* pisafe (U+E010): L<<795.0,490.0>--<796.0,487.0>>/B<<796.0,487.0>-<795.0,489.0>-<795.0,490.0>> = 8.13010235415587 

	* pisafe (U+E010): L<<796.0,485.0>--<797.0,482.0>>/B<<797.0,482.0>-<796.0,484.0>-<796.0,485.0>> = 8.13010235415587 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* a (U+0061): L<<488.0,346.0>--<487.0,106.0>>

	* aacute (U+00E1): L<<488.0,346.0>--<487.0,106.0>>

	* abreve (U+0103): L<<488.0,346.0>--<487.0,106.0>>

	* acircumflex (U+00E2): L<<488.0,346.0>--<487.0,106.0>>

	* adieresis (U+00E4): L<<488.0,346.0>--<487.0,106.0>>

	* agrave (U+00E0): L<<488.0,346.0>--<487.0,106.0>>

	* amacron (U+0101): L<<488.0,346.0>--<487.0,106.0>>

	* aogonek (U+0105): L<<488.0,346.0>--<487.0,106.0>>

	* aring (U+00E5): L<<488.0,346.0>--<487.0,106.0>>

	* aringacute (U+01FB): L<<488.0,346.0>--<487.0,106.0>>

	* atilde (U+00E3): L<<488.0,346.0>--<487.0,106.0>>

	* dotlessi (U+0131): L<<179.0,478.0>--<180.0,21.0>>

	* fi (U+FB01): L<<550.0,478.0>--<551.0,21.0>>

	* h (U+0068): L<<179.0,390.0>--<178.0,21.0>>

	* hbar (U+0127): L<<179.0,390.0>--<178.0,21.0>>

	* hcircumflex (U+0125): L<<179.0,390.0>--<178.0,21.0>>

	* i (U+0069): L<<182.0,478.0>--<183.0,21.0>>

	* ibreve (U+012D): L<<179.0,478.0>--<180.0,21.0>>

	* ij (U+0133): L<<182.0,478.0>--<183.0,21.0>>

	* ij (U+0133): L<<466.0,481.0>--<467.0,-18.0>>

	* iogonek (U+012F): L<<182.0,478.0>--<183.0,21.0>>

	* itilde (U+0129): L<<179.0,478.0>--<180.0,21.0>>

	* j (U+006A): L<<206.0,481.0>--<207.0,-18.0>>

	* k (U+006B): L<<179.0,225.0>--<178.0,21.0>>

	* uni01C8 (U+01C8): L<<743.0,481.0>--<744.0,-18.0>>

	* uni01C9 (U+01C9): L<<458.0,481.0>--<459.0,-18.0>>

	* uni01CB (U+01CB): L<<929.0,481.0>--<930.0,-18.0>>

	* uni01CC (U+01CC): L<<792.0,481.0>--<793.0,-18.0>>

	* uni01CE (U+01CE): L<<488.0,346.0>--<487.0,106.0>>

	* uni01D0 (U+01D0): L<<179.0,478.0>--<180.0,21.0>>

	* uni0201 (U+0201): L<<488.0,346.0>--<487.0,106.0>>

	* uni0203 (U+0203): L<<488.0,346.0>--<487.0,106.0>>

	* uni0209 (U+0209): L<<179.0,478.0>--<180.0,21.0>>

	* uni020B (U+020B): L<<179.0,478.0>--<180.0,21.0>>

	* uni1E2B (U+1E2B): L<<179.0,390.0>--<178.0,21.0>>

	* uni1E2F (U+1E2F): L<<179.0,478.0>--<180.0,21.0>>

	* uni1EA1 (U+1EA1): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EA3 (U+1EA3): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EA5 (U+1EA5): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EA7 (U+1EA7): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EA9 (U+1EA9): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EAB (U+1EAB): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EAD (U+1EAD): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EAF (U+1EAF): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EB1 (U+1EB1): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EB3 (U+1EB3): L<<488.0,346.0>--<487.0,106.0>>

	* uni1EB5 (U+1EB5): L<<488.0,346.0>--<487.0,106.0>> 

	* uni1EB7 (U+1EB7): L<<488.0,346.0>--<487.0,106.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[22] PitagonSans-SemiBold.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Familyname must be unique according to namecheck.fontdata.com (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck">com.google.fonts/check/fontdata_namecheck</a>)</summary><div>


* 💔 **ERROR** Failed to access: http://namecheck.fontdata.com.
		This check relies on the external service http://namecheck.fontdata.com via the internet. While the service cannot be reached or does not respond this check is broken.

		You can exclude this check with the command line option:
		-x com.google.fonts/check/fontdata_namecheck

		Or you can wait until the service is available again.
		If the problem persists please report this issue at: https://github.com/googlefonts/fontbakery/issues

		Original error message:
		<class 'requests.exceptions.ConnectionError'> [code: namecheck-service]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x021A (LATIN CAPITAL LETTER T WITH COMMA BELOW)
 

	- 0x0312 (COMBINING TURNED COMMA ABOVE)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry TRADEMARK on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1175 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ i̛̇ i̛̊ i̛̋ i̤̇ i̤̊ i̤̋ i̦̇ i̦̊ i̦̋ i̧̇ i̧̊ i̧̋ i̮̇ i̮̊ i̮̋ i̱̇ i̱̊ i̱̋ i̵̇ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>


* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Pitagon Sans SemiBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- IJacute

	- caronalt

	- dotbelowcomb.case

	- hookabovecomb.case

	- ijacute

	- uni03020309

	- uni03060309

	- uni031B.case 

	- uni0326.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20BC	Contours detected: 2	Expected: 1

	- Glyph name: uni20BD	Contours detected: 4	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 574 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 551:
plus

Width = 664:
less

Width = 638:
equal

Width = 655:
greater

Width = 629:
logicalnot

Width = 585:
plusminus

Width = 508:
multiply

Width = 628:
divide

Width = 575:
minus

Width = 624:
approxequal

Width = 611:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* petapp (U+E006): L<<297.0,283.0>--<325.0,266.0>> -> L<<325.0,266.0>--<350.0,252.0>>

	* petapp (U+E006): L<<325.0,310.0>--<289.0,331.0>> -> L<<289.0,331.0>--<274.0,339.0>>

	* petapp (U+E006): L<<365.0,287.0>--<325.0,310.0>> -> L<<325.0,310.0>--<289.0,331.0>>

	* petapp (U+E006): L<<374.0,598.0>--<380.0,595.0>> -> L<<380.0,595.0>--<469.0,544.0>>

	* petapp (U+E006): L<<380.0,278.0>--<365.0,287.0>> -> L<<365.0,287.0>--<325.0,310.0>>

	* petapp (U+E006): L<<380.0,595.0>--<469.0,544.0>> -> L<<469.0,544.0>--<514.0,517.0>>

	* petapp (U+E006): L<<382.0,277.0>--<380.0,278.0>> -> L<<380.0,278.0>--<365.0,287.0>>

	* petapp (U+E006): L<<431.0,249.0>--<382.0,277.0>> -> L<<382.0,277.0>--<380.0,278.0>>

	* petapp (U+E006): L<<469.0,544.0>--<514.0,517.0>> -> L<<514.0,517.0>--<532.0,507.0>>

	* petapp (U+E006): L<<470.0,226.0>--<431.0,249.0>> -> L<<431.0,249.0>--<382.0,277.0>>

	* petapp (U+E006): L<<476.0,223.0>--<470.0,226.0>> -> L<<470.0,226.0>--<431.0,249.0>>

	* petapp (U+E006): L<<498.0,210.0>--<476.0,223.0>> -> L<<476.0,223.0>--<470.0,226.0>>

	* petapp (U+E006): L<<505.0,206.0>--<498.0,210.0>> -> L<<498.0,210.0>--<476.0,223.0>>

	* petapp (U+E006): L<<589.0,424.0>--<589.0,429.0>> -> L<<589.0,429.0>--<589.0,434.0>>

	* petapp (U+E006): L<<589.0,429.0>--<589.0,425.0>> -> L<<589.0,425.0>--<589.0,424.0>>

	* petapp (U+E006): L<<590.0,451.0>--<593.0,472.0>> -> L<<593.0,472.0>--<596.0,487.0>>

	* petapp (U+E006): L<<706.0,451.0>--<709.0,451.0>> -> L<<709.0,451.0>--<746.0,451.0>>

	* petapp.minimal (U+E007): L<<279.0,643.0>--<504.0,418.0>> -> L<<504.0,418.0>--<510.0,411.0>>

	* petapp.minimal (U+E007): L<<281.0,347.0>--<361.0,315.0>> -> L<<361.0,315.0>--<436.0,284.0>>

	* petapp.minimal (U+E007): L<<361.0,315.0>--<436.0,284.0>> -> L<<436.0,284.0>--<504.0,257.0>>

	* petapp.minimal (U+E007): L<<389.0,327.0>--<343.0,350.0>> -> L<<343.0,350.0>--<318.0,363.0>>

	* petapp.minimal (U+E007): L<<436.0,284.0>--<504.0,257.0>> -> L<<504.0,257.0>--<605.0,216.0>>

	* petapp.minimal (U+E007): L<<437.0,303.0>--<389.0,327.0>> -> L<<389.0,327.0>--<343.0,350.0>>

	* petapp.minimal (U+E007): L<<439.0,174.0>--<412.0,179.0>> -> L<<412.0,179.0>--<317.0,196.0>>

	* petapp.minimal (U+E007): L<<459.0,292.0>--<437.0,303.0>> -> L<<437.0,303.0>--<389.0,327.0>>

	* petapp.minimal (U+E007): L<<504.0,163.0>--<439.0,174.0>> -> L<<439.0,174.0>--<412.0,179.0>>

	* petapp.minimal (U+E007): L<<504.0,257.0>--<605.0,216.0>> -> L<<605.0,216.0>--<613.0,213.0>>

	* petapp.minimal (U+E007): L<<504.0,269.0>--<459.0,292.0>> -> L<<459.0,292.0>--<437.0,303.0>>

	* petapp.minimal (U+E007): L<<510.0,411.0>--<517.0,405.0>> -> L<<517.0,405.0>--<561.0,361.0>>

	* petapp.minimal (U+E007): L<<517.0,405.0>--<561.0,361.0>> -> L<<561.0,361.0>--<575.0,346.0>>

	* petapp.minimal (U+E007): L<<582.0,149.0>--<504.0,163.0>> -> L<<504.0,163.0>--<439.0,174.0>>

	* petapp.minimal (U+E007): L<<613.0,213.0>--<504.0,269.0>> -> L<<504.0,269.0>--<459.0,292.0>>

	* petapp.minimal (U+E007): L<<726.0,28.0>--<726.0,29.0>> -> L<<726.0,29.0>--<726.0,30.0>>

	* petapp.minimal (U+E007): L<<726.0,29.0>--<726.0,30.0>> -> L<<726.0,30.0>--<726.0,31.0>>

	* petapp.minimal (U+E007): L<<726.0,31.0>--<726.0,31.0>> -> L<<726.0,31.0>--<726.0,31.0>>

	* petapp.minimal (U+E007): L<<729.0,69.0>--<729.0,68.0>> -> L<<729.0,68.0>--<729.0,59.0>>

	* petapp.minimal (U+E007): L<<729.0,69.0>--<729.0,71.0>> -> L<<729.0,71.0>--<729.0,72.0>>

	* petapp.minimal (U+E007): L<<729.0,72.0>--<729.0,69.0>> -> L<<729.0,69.0>--<729.0,68.0>>

	* petapp.minimal (U+E007): L<<729.0,72.0>--<729.0,72.0>> -> L<<729.0,72.0>--<729.0,72.0>>

	* petapp.minimal (U+E007): L<<729.0,73.0>--<729.0,72.0>> -> L<<729.0,72.0>--<729.0,69.0>>

	* petapp.minimal (U+E007): L<<737.0,151.0>--<734.0,122.0>> -> L<<734.0,122.0>--<729.0,72.0>>

	* petapp.minimal (U+E007): L<<738.0,163.0>--<737.0,151.0>> -> L<<737.0,151.0>--<734.0,122.0>>

	* petapp.minimal (U+E007): L<<739.0,182.0>--<738.0,163.0>> -> L<<738.0,163.0>--<737.0,151.0>>

	* petapp.minimal (U+E007): L<<740.0,195.0>--<739.0,182.0>> -> L<<739.0,182.0>--<738.0,163.0>>

	* petapp.wpda (U+E008): L<<601.0,115.0>--<589.0,110.0>> -> L<<589.0,110.0>--<578.0,106.0>>

	* petapp.wpda (U+E008): L<<609.0,118.0>--<601.0,115.0>> -> L<<601.0,115.0>--<589.0,110.0>>

	* petapp.wpda (U+E008): L<<630.0,130.0>--<618.0,123.0>> -> L<<618.0,123.0>--<609.0,118.0>>

	* piads (U+E001): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* piads (U+E001): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* picall (U+E009): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<448.0,729.0>>

	* picall (U+E009): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<852.0,504.0>>

	* pioffice (U+E002): L<<138.0,504.0>--<142.0,507.0>> -> L<<142.0,507.0>--<447.0,729.0>>

	* pisafe (U+E010): L<<190.0,337.0>--<190.0,457.0>> -> L<<190.0,457.0>--<190.0,462.0>>

	* pisafe (U+E010): L<<218.0,644.0>--<223.0,646.0>> -> L<<223.0,646.0>--<257.0,658.0>>

	* pisafe (U+E010): L<<223.0,646.0>--<257.0,658.0>> -> L<<257.0,658.0>--<396.0,709.0>>

	* pisafe (U+E010): L<<257.0,658.0>--<396.0,709.0>> -> L<<396.0,709.0>--<494.0,744.0>>

	* pisafe (U+E010): L<<495.0,744.0>--<593.0,709.0>> -> L<<593.0,709.0>--<732.0,658.0>>

	* pisafe (U+E010): L<<593.0,709.0>--<732.0,658.0>> -> L<<732.0,658.0>--<766.0,646.0>>

	* pisafe (U+E010): L<<732.0,658.0>--<766.0,646.0>> -> L<<766.0,646.0>--<771.0,644.0>>

	* pisign (U+E005): L<<542.0,729.0>--<848.0,507.0>> -> L<<848.0,507.0>--<851.0,505.0>>

	* pitagon (U+E000): L<<138.0,505.0>--<142.0,508.0>> -> L<<142.0,508.0>--<448.0,730.0>>

	* pitagon (U+E000): L<<229.0,57.0>--<112.0,415.0>> -> L<<112.0,415.0>--<110.0,420.0>>

	* pitagon (U+E000): L<<543.0,730.0>--<848.0,508.0>> -> L<<848.0,508.0>--<852.0,505.0>>

	* pitagram (U+E003): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>>

	* piweb (U+E004): L<<791.0,477.0>--<788.0,479.0>> -> L<<788.0,479.0>--<534.0,663.0>>

	* sparks (U+E011): L<<130.0,741.0>--<219.0,709.0>> -> L<<219.0,709.0>--<229.0,706.0>>

	* sparks (U+E011): L<<219.0,709.0>--<229.0,706.0>> -> L<<229.0,706.0>--<407.0,642.0>>

	* sparks (U+E011): L<<229.0,706.0>--<407.0,642.0>> -> L<<407.0,642.0>--<435.0,632.0>>

	* sparks (U+E011): L<<305.0,554.0>--<372.0,497.0>> -> L<<372.0,497.0>--<390.0,480.0>>

	* sparks (U+E011): L<<389.0,340.0>--<391.0,341.0>> -> L<<391.0,341.0>--<487.0,399.0>>

	* sparks (U+E011): L<<415.0,95.0>--<126.0,596.0>> -> L<<126.0,596.0>--<78.0,680.0>>

	* sparks (U+E011): L<<424.0,589.0>--<383.0,585.0>> -> L<<383.0,585.0>--<363.0,583.0>>

	* sparks (U+E011): L<<444.0,613.0>--<440.0,604.0>> -> L<<440.0,604.0>--<438.0,598.0>>

	* sparks (U+E011): L<<457.0,22.0>--<415.0,95.0>> -> L<<415.0,95.0>--<126.0,596.0>>

	* sparks (U+E011): L<<503.0,399.0>--<598.0,341.0>> -> L<<598.0,341.0>--<600.0,340.0>>

	* sparks (U+E011): L<<554.0,632.0>--<589.0,645.0>> -> L<<589.0,645.0>--<760.0,706.0>>

	* sparks (U+E011): L<<573.0,94.0>--<546.0,47.0>> -> L<<546.0,47.0>--<532.0,22.0>>

	* sparks (U+E011): L<<589.0,645.0>--<760.0,706.0>> -> L<<760.0,706.0>--<785.0,714.0>>

	* sparks (U+E011): L<<599.0,480.0>--<618.0,497.0>> -> L<<618.0,497.0>--<685.0,554.0>>

	* sparks (U+E011): L<<606.0,585.0>--<571.0,588.0>> -> L<<571.0,588.0>--<563.0,589.0>>

	* sparks (U+E011): L<<644.0,582.0>--<606.0,585.0>> -> L<<606.0,585.0>--<571.0,588.0>>

	* sparks (U+E011): L<<645.0,582.0>--<644.0,582.0>> -> L<<644.0,582.0>--<606.0,585.0>>

	* sparks (U+E011): L<<676.0,579.0>--<645.0,582.0>> -> L<<645.0,582.0>--<644.0,582.0>>

	* sparks (U+E011): L<<677.0,579.0>--<676.0,579.0>> -> L<<676.0,579.0>--<645.0,582.0>>

	* sparks (U+E011): L<<732.0,369.0>--<573.0,94.0>> -> L<<573.0,94.0>--<546.0,47.0>>

	* sparks (U+E011): L<<760.0,706.0>--<785.0,714.0>> -> L<<785.0,714.0>--<859.0,741.0>>

	* sparks (U+E011): L<<869.0,606.0>--<732.0,369.0>> -> L<<732.0,369.0>--<573.0,94.0>>

	* sparks (U+E011): L<<911.0,679.0>--<869.0,606.0>> -> L<<869.0,606.0>--<732.0,369.0>> 

	* sparks (U+E011): L<<912.0,681.0>--<911.0,679.0>> -> L<<911.0,679.0>--<869.0,606.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<299.0,448.0>-<299.0,447.0>-<300.0,445.0>>/L<<300.0,445.0>--<299.0,448.0>> = 8.130102354155916

	* petapp (U+E006): B<<319.0,259.0>-<312.0,273.0>-<297.0,283.0>>/L<<297.0,283.0>--<325.0,266.0>> = 2.4263358316022132

	* petapp (U+E006): B<<322.0,413.0>-<323.0,412.0>-<325.0,411.0>>/L<<325.0,411.0>--<322.0,413.0>> = 7.125016348901757

	* petapp (U+E006): B<<335.0,402.0>-<337.0,401.0>-<338.0,400.0>>/L<<338.0,400.0>--<335.0,402.0>> = 11.309932474020195

	* petapp (U+E006): B<<340.0,399.0>-<341.0,398.0>-<343.0,397.0>>/L<<343.0,397.0>--<340.0,399.0>> = 7.125016348901757

	* petapp (U+E006): B<<407.0,83.0>-<409.0,82.0>-<411.0,80.0>>/L<<411.0,80.0>--<407.0,83.0>> = 8.13010235415596

	* petapp (U+E006): B<<491.0,62.0>-<493.0,62.0>-<496.0,63.0>>/L<<496.0,63.0>--<491.0,62.0>> = 7.125016348901757

	* petapp (U+E006): B<<511.0,60.0>-<513.0,60.0>-<515.0,61.0>>/L<<515.0,61.0>--<511.0,60.0>> = 12.528807709151463

	* petapp (U+E006): B<<517.0,61.0>-<519.0,61.0>-<521.0,62.0>>/L<<521.0,62.0>--<517.0,61.0>> = 12.528807709151463

	* petapp (U+E006): B<<527.0,63.0>-<526.0,63.0>-<524.0,62.0>>/L<<524.0,62.0>--<527.0,63.0>> = 8.13010235415587

	* petapp (U+E006): B<<532.0,92.0>-<533.0,94.0>-<535.0,96.0>>/L<<535.0,96.0>--<532.0,92.0>> = 8.130102354155916

	* petapp (U+E006): B<<533.0,178.0>-<533.0,179.0>-<532.0,181.0>>/L<<532.0,181.0>--<533.0,178.0>> = 8.13010235415587

	* petapp (U+E006): B<<535.0,286.0>-<533.0,287.0>-<532.0,288.0>>/L<<532.0,288.0>--<535.0,286.0>> = 11.309932474020227

	* petapp (U+E006): B<<537.0,407.0>-<535.0,408.0>-<534.0,409.0>>/L<<534.0,409.0>--<537.0,407.0>> = 11.309932474020227

	* petapp (U+E006): B<<542.0,115.0>-<542.0,116.0>-<543.0,118.0>>/L<<543.0,118.0>--<542.0,115.0>> = 8.130102354155916

	* petapp (U+E006): B<<545.0,133.0>-<546.0,134.0>-<546.0,137.0>>/L<<546.0,137.0>--<545.0,133.0>> = 14.036243467926484

	* petapp (U+E006): B<<581.0,353.0>-<580.0,355.0>-<580.0,357.0>>/L<<580.0,357.0>--<581.0,353.0>> = 14.036243467926484

	* petapp (U+E006): B<<582.0,224.0>-<582.0,225.0>-<581.0,227.0>>/L<<581.0,227.0>--<582.0,224.0>> = 8.13010235415587

	* petapp (U+E006): B<<588.0,157.0>-<589.0,154.0>-<589.0,152.0>>/L<<589.0,152.0>--<588.0,157.0>> = 11.309932474020227

	* petapp (U+E006): B<<590.0,411.0>-<590.0,410.0>-<591.0,408.0>>/L<<591.0,408.0>--<590.0,411.0>> = 8.130102354155916

	* petapp (U+E006): B<<592.0,394.0>-<591.0,396.0>-<591.0,398.0>>/L<<591.0,398.0>--<592.0,394.0>> = 14.036243467926484

	* petapp (U+E006): B<<612.0,346.0>-<612.0,345.0>-<613.0,343.0>>/L<<613.0,343.0>--<612.0,346.0>> = 8.130102354155916

	* petapp (U+E006): B<<614.0,326.0>-<615.0,325.0>-<616.0,323.0>>/L<<616.0,323.0>--<614.0,326.0>> = 7.125016348901705

	* petapp (U+E006): B<<627.0,324.0>-<627.0,323.0>-<628.0,321.0>>/L<<628.0,321.0>--<627.0,324.0>> = 8.130102354155916

	* petapp (U+E006): B<<650.0,356.0>-<650.0,355.0>-<651.0,353.0>>/L<<651.0,353.0>--<650.0,356.0>> = 8.130102354155916

	* petapp (U+E006): B<<657.0,125.0>-<658.0,126.0>-<660.0,127.0>>/L<<660.0,127.0>--<657.0,125.0>> = 7.125016348901757

	* petapp (U+E006): B<<679.0,56.0>-<680.0,54.0>-<682.0,53.0>>/L<<682.0,53.0>--<678.0,56.0>> = 10.304846468766009

	* petapp (U+E006): B<<730.0,22.0>-<729.0,23.0>-<727.0,24.0>>/L<<727.0,24.0>--<730.0,22.0>> = 7.125016348901757

	* petapp (U+E006): B<<743.0,6.0>-<743.0,7.0>-<742.0,9.0>>/L<<742.0,9.0>--<743.0,6.0>> = 8.13010235415587

	* petapp (U+E006): L<<290.0,476.0>--<289.0,479.0>>/B<<289.0,479.0>-<290.0,477.0>-<290.0,476.0>> = 8.130102354155916

	* petapp (U+E006): L<<307.0,431.0>--<306.0,434.0>>/B<<306.0,434.0>-<307.0,432.0>-<307.0,431.0>> = 8.130102354155916

	* petapp (U+E006): L<<325.0,411.0>--<322.0,413.0>>/B<<322.0,413.0>-<323.0,412.0>-<325.0,411.0>> = 11.309932474020195

	* petapp (U+E006): L<<338.0,400.0>--<335.0,402.0>>/B<<335.0,402.0>-<337.0,401.0>-<338.0,400.0>> = 7.125016348901757

	* petapp (U+E006): L<<343.0,397.0>--<340.0,399.0>>/B<<340.0,399.0>-<341.0,398.0>-<343.0,397.0>> = 11.309932474020195

	* petapp (U+E006): L<<390.0,112.0>--<389.0,115.0>>/B<<389.0,115.0>-<390.0,113.0>-<390.0,112.0>> = 8.130102354155916

	* petapp (U+E006): L<<411.0,80.0>--<407.0,83.0>>/B<<407.0,83.0>-<409.0,82.0>-<411.0,80.0>> = 10.304846468766009

	* petapp (U+E006): L<<496.0,63.0>--<491.0,62.0>>/B<<491.0,62.0>-<493.0,62.0>-<496.0,63.0>> = 11.309932474020195

	* petapp (U+E006): L<<499.0,209.0>--<505.0,206.0>>/L<<505.0,206.0>--<498.0,210.0>> = 3.1798301198640497

	* petapp (U+E006): L<<510.0,70.0>--<507.0,69.0>>/B<<507.0,69.0>-<509.0,70.0>-<510.0,70.0>> = 8.130102354155916

	* petapp (U+E006): L<<515.0,61.0>--<511.0,60.0>>/B<<511.0,60.0>-<513.0,60.0>-<515.0,61.0>> = 14.036243467926484

	* petapp (U+E006): L<<520.0,78.0>--<516.0,75.0>>/B<<516.0,75.0>-<518.0,76.0>-<520.0,78.0>> = 10.304846468766009

	* petapp (U+E006): L<<521.0,62.0>--<517.0,61.0>>/B<<517.0,61.0>-<519.0,61.0>-<521.0,62.0>> = 14.036243467926484

	* petapp (U+E006): L<<530.0,63.0>--<534.0,64.0>>/B<<534.0,64.0>-<531.0,64.0>-<530.0,63.0>> = 14.036243467926484

	* petapp (U+E006): L<<532.0,288.0>--<535.0,286.0>>/B<<535.0,286.0>-<533.0,287.0>-<532.0,288.0>> = 7.125016348901757

	* petapp (U+E006): L<<534.0,409.0>--<537.0,407.0>>/B<<537.0,407.0>-<535.0,408.0>-<534.0,409.0>> = 7.125016348901757

	* petapp (U+E006): L<<535.0,176.0>--<536.0,173.0>>/B<<536.0,173.0>-<535.0,175.0>-<535.0,176.0>> = 8.13010235415587

	* petapp (U+E006): L<<535.0,96.0>--<532.0,92.0>>/B<<532.0,92.0>-<533.0,94.0>-<535.0,96.0>> = 10.304846468765973

	* petapp (U+E006): L<<537.0,65.0>--<540.0,66.0>>/B<<540.0,66.0>-<538.0,65.0>-<537.0,65.0>> = 8.13010235415587

	* petapp (U+E006): L<<552.0,69.0>--<549.0,68.0>>/B<<549.0,68.0>-<551.0,69.0>-<552.0,69.0>> = 8.130102354155916

	* petapp (U+E006): L<<577.0,238.0>--<578.0,234.0>>/B<<578.0,234.0>-<578.0,236.0>-<577.0,238.0>> = 14.036243467926484

	* petapp (U+E006): L<<580.0,357.0>--<581.0,353.0>>/B<<581.0,353.0>-<580.0,355.0>-<580.0,357.0>> = 12.528807709151492

	* petapp (U+E006): L<<587.0,201.0>--<588.0,198.0>>/B<<588.0,198.0>-<587.0,200.0>-<587.0,201.0>> = 8.13010235415587

	* petapp (U+E006): L<<587.0,330.0>--<588.0,327.0>>/B<<588.0,327.0>-<587.0,329.0>-<587.0,330.0>> = 8.13010235415587

	* petapp (U+E006): L<<589.0,152.0>--<588.0,157.0>>/B<<588.0,157.0>-<589.0,154.0>-<589.0,152.0>> = 7.125016348901757

	* petapp (U+E006): L<<613.0,328.0>--<612.0,331.0>>/B<<612.0,331.0>-<613.0,329.0>-<613.0,328.0>> = 8.130102354155916

	* petapp (U+E006): L<<616.0,323.0>--<614.0,326.0>>/B<<614.0,326.0>-<615.0,325.0>-<616.0,323.0>> = 11.309932474020227

	* petapp (U+E006): L<<660.0,127.0>--<657.0,125.0>>/B<<657.0,125.0>-<658.0,126.0>-<660.0,127.0>> = 11.309932474020195

	* petapp (U+E006): L<<668.0,142.0>--<667.0,139.0>>/B<<667.0,139.0>-<668.0,141.0>-<668.0,142.0>> = 8.130102354155916

	* petapp (U+E006): L<<674.0,441.0>--<677.0,442.0>>/B<<677.0,442.0>-<675.0,441.0>-<674.0,441.0>> = 8.13010235415587

	* petapp (U+E006): L<<681.0,219.0>--<682.0,216.0>>/B<<682.0,216.0>-<681.0,218.0>-<681.0,219.0>> = 8.13010235415587

	* petapp (U+E006): L<<690.0,448.0>--<693.0,449.0>>/B<<693.0,449.0>-<691.0,448.0>-<690.0,448.0>> = 8.13010235415587

	* petapp (U+E006): L<<706.0,267.0>--<703.0,268.0>>/B<<703.0,268.0>-<705.0,267.0>-<706.0,267.0>> = 8.130102354155916

	* petapp (U+E006): L<<718.0,29.0>--<721.0,28.0>>/B<<721.0,28.0>-<719.0,29.0>-<718.0,29.5>> = 8.13010235415587

	* petapp (U+E006): L<<727.0,24.0>--<730.0,22.0>>/B<<730.0,22.0>-<729.0,23.0>-<727.0,24.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<649.0,193.0>-<648.0,193.0>-<646.0,194.0>>/L<<646.0,194.0>--<649.0,193.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<666.0,502.0>-<665.0,501.0>-<663.0,500.0>>/L<<663.0,500.0>--<666.0,502.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<692.0,147.0>-<692.0,148.0>-<691.0,150.0>>/L<<691.0,150.0>--<692.0,147.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<698.0,138.0>-<698.0,139.0>-<697.0,141.0>>/L<<697.0,141.0>--<698.0,138.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<703.0,201.0>-<702.0,203.0>-<701.0,204.0>>/L<<701.0,204.0>--<703.0,201.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<704.0,127.0>-<703.0,129.0>-<702.0,132.0>>/L<<702.0,132.0>--<704.0,127.0>> = 3.3664606634297236

	* petapp.minimal (U+E007): B<<723.5,10.0>-<723.0,5.0>-<722.0,0.0>>/B<<722.0,0.0>-<722.0,9.0>-<720.0,16.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<724.0,140.0>-<723.0,143.0>-<723.0,145.0>>/L<<723.0,145.0>--<724.0,140.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<233.0,500.0>--<233.0,744.0>>/B<<233.0,744.0>-<236.0,686.0>-<276.0,646.0>> = 2.9609361341637563

	* petapp.minimal (U+E007): L<<561.0,361.0>--<575.0,346.0>>/B<<575.0,346.0>-<572.0,350.0>-<568.5,353.5>> = 6.155168343273918

	* petapp.minimal (U+E007): L<<622.0,400.0>--<621.0,405.0>>/B<<621.0,405.0>-<621.0,402.0>-<622.0,400.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<628.0,206.0>--<631.0,204.0>>/B<<631.0,204.0>-<629.0,205.0>-<628.0,206.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<663.0,500.0>--<666.0,502.0>>/B<<666.0,502.0>-<665.0,501.0>-<663.0,500.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<673.0,505.0>--<677.0,507.0>>/B<<677.0,507.0>-<674.0,506.0>-<673.0,505.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<679.0,240.0>--<680.0,237.0>>/B<<680.0,237.0>-<679.0,239.0>-<679.0,240.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<688.0,227.0>--<689.0,224.0>>/B<<689.0,224.0>-<688.0,226.0>-<688.0,227.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<694.0,218.0>--<695.0,215.0>>/B<<695.0,215.0>-<694.0,217.0>-<694.0,218.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<701.0,204.0>--<703.0,201.0>>/B<<703.0,201.0>-<702.0,203.0>-<701.0,204.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<702.0,132.0>--<704.0,127.0>>/B<<704.0,127.0>-<703.0,129.0>-<702.0,132.0>> = 4.763641690726143

	* petapp.minimal (U+E007): L<<711.0,114.0>--<712.0,111.0>>/B<<712.0,111.0>-<711.0,113.0>-<711.0,114.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<714.0,175.0>--<715.0,172.0>>/B<<715.0,172.0>-<714.0,174.0>-<714.0,175.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<722.0,79.0>--<723.0,76.0>>/B<<723.0,76.0>-<722.0,78.0>-<722.0,79.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<723.0,145.0>--<724.0,140.0>>/B<<724.0,140.0>-<723.0,143.0>-<723.0,145.0>> = 7.125016348901705

	* petapp.wpda (U+E008): B<<486.0,2.0>-<483.0,5.0>-<483.0,6.0>>/L<<483.0,6.0>--<482.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<207.0,206.0>--<202.0,203.0>>/B<<202.0,203.0>-<204.0,204.0>-<205.0,203.0>> = 4.398705354995426

	* pisafe (U+E010): B<<197.0,501.0>-<197.0,499.0>-<196.0,497.0>>/L<<196.0,497.0>--<197.0,501.0>> = 12.528807709151492

	* pisafe (U+E010): B<<215.0,540.0>-<215.0,539.0>-<214.0,537.0>>/L<<214.0,537.0>--<215.0,540.0>> = 8.13010235415587

	* pisafe (U+E010): B<<230.0,559.0>-<229.0,558.0>-<228.0,556.0>>/L<<228.0,556.0>--<230.0,559.0>> = 7.125016348901757

	* pisafe (U+E010): B<<246.0,573.0>-<244.0,572.0>-<243.0,571.0>>/L<<243.0,571.0>--<246.0,573.0>> = 11.309932474020227

	* pisafe (U+E010): B<<764.0,552.0>-<763.0,554.0>-<762.0,555.0>>/L<<762.0,555.0>--<764.0,552.0>> = 11.309932474020195

	* pisafe (U+E010): B<<776.0,535.0>-<776.0,536.0>-<775.0,538.0>>/L<<775.0,538.0>--<776.0,535.0>> = 8.13010235415587

	* pisafe (U+E010): B<<784.0,521.0>-<784.0,522.0>-<783.0,524.0>>/L<<783.0,524.0>--<784.0,521.0>> = 8.13010235415587

	* pisafe (U+E010): L<<196.0,497.0>--<197.0,501.0>>/B<<197.0,501.0>-<197.0,499.0>-<196.0,497.0>> = 14.036243467926484

	* pisafe (U+E010): L<<209.0,528.0>--<210.0,531.0>>/B<<210.0,531.0>-<209.0,529.0>-<209.0,528.0>> = 8.13010235415587

	* pisafe (U+E010): L<<228.0,556.0>--<230.0,559.0>>/B<<230.0,559.0>-<229.0,558.0>-<228.0,556.0>> = 11.309932474020195

	* pisafe (U+E010): L<<243.0,571.0>--<246.0,573.0>>/B<<246.0,573.0>-<244.0,572.0>-<243.0,571.0>> = 7.125016348901757

	* pisafe (U+E010): L<<732.0,582.0>--<735.0,580.0>>/B<<735.0,580.0>-<734.0,581.0>-<732.0,582.0>> = 11.309932474020227

	* pisafe (U+E010): L<<762.0,555.0>--<764.0,552.0>>/B<<764.0,552.0>-<763.0,554.0>-<762.0,555.0>> = 7.125016348901757

	* pisafe (U+E010): L<<793.0,497.0>--<794.0,492.0>>/B<<794.0,492.0>-<794.0,495.0>-<793.0,497.0>> = 11.309932474020195

	* pisafe (U+E010): L<<795.0,490.0>--<796.0,487.0>>/B<<796.0,487.0>-<795.0,489.0>-<795.0,490.0>> = 8.13010235415587 

	* pisafe (U+E010): L<<796.0,485.0>--<797.0,482.0>>/B<<797.0,482.0>-<796.0,484.0>-<796.0,485.0>> = 8.13010235415587 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* a (U+0061): L<<497.0,345.0>--<496.0,106.0>>

	* aacute (U+00E1): L<<497.0,345.0>--<496.0,106.0>>

	* abreve (U+0103): L<<497.0,345.0>--<496.0,106.0>>

	* acircumflex (U+00E2): L<<497.0,345.0>--<496.0,106.0>>

	* adieresis (U+00E4): L<<497.0,345.0>--<496.0,106.0>>

	* agrave (U+00E0): L<<497.0,345.0>--<496.0,106.0>>

	* amacron (U+0101): L<<497.0,345.0>--<496.0,106.0>>

	* aogonek (U+0105): L<<497.0,345.0>--<496.0,106.0>>

	* aring (U+00E5): L<<497.0,345.0>--<496.0,106.0>>

	* aringacute (U+01FB): L<<497.0,345.0>--<496.0,106.0>>

	* atilde (U+00E3): L<<497.0,345.0>--<496.0,106.0>>

	* dotlessi (U+0131): L<<197.0,475.0>--<198.0,24.0>>

	* fi (U+FB01): L<<578.0,475.0>--<579.0,24.0>>

	* h (U+0068): L<<198.0,382.0>--<196.0,24.0>>

	* hbar (U+0127): L<<198.0,382.0>--<196.0,24.0>>

	* hcircumflex (U+0125): L<<198.0,382.0>--<196.0,24.0>>

	* i (U+0069): L<<200.0,475.0>--<201.0,24.0>>

	* ibreve (U+012D): L<<197.0,475.0>--<198.0,24.0>>

	* ij (U+0133): L<<200.0,475.0>--<201.0,24.0>>

	* ij (U+0133): L<<494.0,480.0>--<495.0,-11.0>>

	* iogonek (U+012F): L<<200.0,475.0>--<201.0,24.0>>

	* itilde (U+0129): L<<197.0,475.0>--<198.0,24.0>>

	* j (U+006A): L<<221.0,480.0>--<222.0,-11.0>>

	* k (U+006B): L<<198.0,671.0>--<197.0,316.0>>

	* uni01C8 (U+01C8): L<<767.0,480.0>--<768.0,-11.0>>

	* uni01C9 (U+01C9): L<<487.0,480.0>--<488.0,-11.0>>

	* uni01CB (U+01CB): L<<945.0,480.0>--<946.0,-11.0>>

	* uni01CC (U+01CC): L<<819.0,480.0>--<820.0,-11.0>>

	* uni01CE (U+01CE): L<<497.0,345.0>--<496.0,106.0>>

	* uni01D0 (U+01D0): L<<197.0,475.0>--<198.0,24.0>>

	* uni0201 (U+0201): L<<497.0,345.0>--<496.0,106.0>>

	* uni0203 (U+0203): L<<497.0,345.0>--<496.0,106.0>>

	* uni0209 (U+0209): L<<197.0,475.0>--<198.0,24.0>>

	* uni020B (U+020B): L<<197.0,475.0>--<198.0,24.0>>

	* uni1E2B (U+1E2B): L<<198.0,382.0>--<196.0,24.0>>

	* uni1E2F (U+1E2F): L<<197.0,475.0>--<198.0,24.0>>

	* uni1E9E (U+1E9E): L<<211.0,435.0>--<210.0,24.0>>

	* uni1EA1 (U+1EA1): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EA3 (U+1EA3): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EA5 (U+1EA5): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EA7 (U+1EA7): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EA9 (U+1EA9): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EAB (U+1EAB): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EAD (U+1EAD): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EAF (U+1EAF): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EB1 (U+1EB1): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EB3 (U+1EB3): L<<497.0,345.0>--<496.0,106.0>>

	* uni1EB5 (U+1EB5): L<<497.0,345.0>--<496.0,106.0>> 

	* uni1EB7 (U+1EB7): L<<497.0,345.0>--<496.0,106.0>> [code: found-semi-vertical]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 6 | 42 | 79 | 698 | 37 | 510 | 0 |
| 0% | 3% | 6% | 51% | 3% | 37% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
