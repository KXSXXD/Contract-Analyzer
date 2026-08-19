

TRAINING_DATA = [
    # ---------------- Indemnification ----------------
    ("Each party shall indemnify and hold harmless the other party from and against any third-party claims arising directly out of its own gross negligence or willful misconduct in performing this Agreement.", "Indemnification"),
    ("Client shall indemnify, defend, and hold harmless Vendor and its officers, directors, and employees from any and all claims, losses, damages, and expenses of any kind whatsoever, whether or not arising from Vendor's own negligence.", "Indemnification"),
    ("Contractor agrees to indemnify Company against losses caused by Contractor's breach of this Agreement, limited to direct damages actually incurred.", "Indemnification"),
    ("Supplier shall indemnify Buyer for any and all claims without limitation, including claims arising from Buyer's own acts or omissions, in perpetuity.", "Indemnification"),
    ("Each party's indemnification obligations under this Section shall be limited to claims resulting from that party's breach of its representations and warranties.", "Indemnification"),
    ("The Consultant shall have no obligation to indemnify the Client except to the extent a claim results from the Consultant's fraud.", "Indemnification"),
    ("Party A agrees to indemnify Party B for any claim, demand, or proceeding of any nature arising in connection with this Agreement, regardless of cause, fault, or foreseeability.", "Indemnification"),

    # ---------------- Limitation of Liability ----------------
    ("In no event shall either party's aggregate liability under this Agreement exceed the total fees paid in the twelve months preceding the claim.", "Limitation of Liability"),
    ("Neither party shall be liable to the other for any indirect, incidental, special, or consequential damages arising out of this Agreement.", "Limitation of Liability"),
    ("Vendor's total liability, whether in contract, tort, or otherwise, shall in no event exceed one hundred dollars, regardless of the nature or number of claims.", "Limitation of Liability"),
    ("There shall be no limitation or cap of any kind on Client's liability to Vendor under this Agreement, including for indirect and consequential damages.", "Limitation of Liability"),
    ("Each party's liability for breach of confidentiality obligations shall not be subject to the general liability cap set out in this Section.", "Limitation of Liability"),
    ("Company's liability shall be limited solely at Company's discretion, and Company reserves the right to disclaim all liability at any time without notice.", "Limitation of Liability"),

    # ---------------- Termination ----------------
    ("Either party may terminate this Agreement for convenience upon sixty (60) days' prior written notice to the other party.", "Termination"),
    ("Company may terminate this Agreement immediately and without notice at its sole and absolute discretion for any reason or no reason whatsoever.", "Termination"),
    ("This Agreement may be terminated by either party if the other party materially breaches any provision and fails to cure such breach within thirty (30) days of written notice.", "Termination"),
    ("Upon termination for any reason, all fees paid to date shall be deemed fully earned and non-refundable, and Client shall remain liable for the full remaining contract value.", "Termination"),
    ("Employee may resign from this position by providing two weeks' written notice to the Company.", "Termination"),
    ("Client may not terminate this Agreement under any circumstances prior to the expiration of the initial five-year term.", "Termination"),

    # ---------------- Confidentiality ----------------
    ("Each party agrees to protect the other party's Confidential Information using the same degree of care it uses for its own confidential information, but no less than reasonable care.", "Confidentiality"),
    ("Recipient shall keep all Confidential Information strictly confidential and shall not disclose it to any third party without Discloser's prior written consent, for a period of five years following disclosure.", "Confidentiality"),
    ("The confidentiality obligations in this Section shall survive termination of this Agreement in perpetuity and apply even to information that later becomes publicly available.", "Confidentiality"),
    ("Confidential Information does not include information that is or becomes publicly available through no fault of the Recipient, or that was already known to Recipient prior to disclosure.", "Confidentiality"),
    ("Employee agrees never to disclose any information learned during employment, including information that is general industry knowledge, for the rest of Employee's life.", "Confidentiality"),

    # ---------------- Payment Terms ----------------
    ("Client shall pay all undisputed invoices within thirty (30) days of the invoice date via bank transfer.", "Payment Terms"),
    ("Late payments shall accrue interest at a rate of 1.5% per month, or the maximum rate permitted by law, whichever is lower.", "Payment Terms"),
    ("All fees are due immediately upon signing and are non-refundable under any circumstances, including if Vendor fails to deliver any services.", "Payment Terms"),
    ("Company reserves the right to unilaterally increase fees at any time during the term without prior notice to Client.", "Payment Terms"),
    ("Payment shall be made in the currency specified in the applicable purchase order, and each party shall bear its own bank transfer fees.", "Payment Terms"),

    # ---------------- Intellectual Property ----------------
    ("All intellectual property developed by Contractor specifically for Client under this Agreement shall be owned by Client upon full payment.", "Intellectual Property"),
    ("Contractor hereby assigns to Company all right, title, and interest in any and all inventions, works, and ideas Contractor has ever created, including those unrelated to this Agreement.", "Intellectual Property"),
    ("Each party retains ownership of its pre-existing intellectual property, and no license is granted except as expressly set out in this Agreement.", "Intellectual Property"),
    ("Company shall own all IP created by Contractor during the term of this engagement, including IP created entirely on Contractor's own time using Contractor's own equipment.", "Intellectual Property"),
    ("Licensee is granted a limited, non-exclusive, non-transferable license to use the Software solely for its internal business purposes.", "Intellectual Property"),

    # ---------------- Non-Compete / Non-Solicitation ----------------
    ("For a period of twelve (12) months following termination, Employee shall not work for a direct competitor within the same metropolitan area.", "Non-Compete"),
    ("Employee agrees not to engage in any business anywhere in the world that competes with Company in any way, for a period of ten years after termination.", "Non-Compete"),
    ("During the term and for six months thereafter, neither party shall solicit for employment any employee of the other party who was involved in this engagement.", "Non-Compete"),
    ("This non-compete restriction shall not apply if Employee is terminated without cause.", "Non-Compete"),

    # ---------------- Governing Law / Dispute Resolution ----------------
    ("This Agreement shall be governed by and construed in accordance with the laws of the State of Delaware, without regard to its conflict of laws principles.", "Governing Law"),
    ("This Agreement and any dispute arising out of it shall be governed exclusively by the laws of England and Wales.", "Governing Law"),
    ("The validity, interpretation, and performance of this Agreement shall be governed by the laws of Singapore.", "Governing Law"),
    ("Any dispute arising under this Agreement shall be resolved exclusively through binding arbitration administered by the ICC, with each party bearing its own costs.", "Dispute Resolution"),
    ("All disputes must be brought exclusively in the courts located in Company's home jurisdiction, and Client irrevocably waives any right to a jury trial or class action.", "Dispute Resolution"),
    ("The parties agree to attempt in good faith to resolve any dispute through informal negotiation before pursuing formal legal remedies.", "Dispute Resolution"),

    # ---------------- Force Majeure ----------------
    ("Neither party shall be liable for any failure or delay in performance due to causes beyond its reasonable control, including natural disasters, war, or government action.", "Force Majeure"),
    ("Vendor's force majeure protections shall not extend to any obligation to make payments due under this Agreement.", "Force Majeure"),
    ("Client shall bear all risk of delay for any reason whatsoever, including events of force majeure affecting Vendor, and no relief shall be granted to Vendor under any circumstances.", "Force Majeure"),

    # ---------------- Warranty ----------------
    ("Vendor warrants that the Services will be performed in a professional and workmanlike manner consistent with generally accepted industry standards.", "Warranty"),
    ("The Software is provided strictly 'as is' with no warranties of any kind whatsoever, express or implied, including no warranty of merchantability or fitness for a particular purpose.", "Warranty"),
    ("Vendor warrants good title to the goods and that they are free of all liens and encumbrances at the time of delivery.", "Warranty"),

    # ---------------- Assignment ----------------
    ("Neither party may assign this Agreement without the prior written consent of the other party, such consent not to be unreasonably withheld.", "Assignment"),
    ("Company may freely assign this Agreement, in whole or in part, to any third party at any time without notice to or consent from Client.", "Assignment"),
    ("This Agreement shall be binding upon and inure to the benefit of the parties and their respective successors and permitted assigns.", "Assignment"),

    # ---------------- Data Protection ----------------
    ("Each party shall comply with applicable data protection laws in connection with any personal data processed under this Agreement.", "Data Protection"),
    ("Vendor shall implement reasonable technical and organizational measures to protect personal data against unauthorized access, loss, or disclosure.", "Data Protection"),
    ("Client grants Vendor an unrestricted right to use, sell, and share any personal data collected under this Agreement for any purpose, in perpetuity.", "Data Protection"),

    # ---------------- Insurance ----------------
    ("Contractor shall maintain commercial general liability insurance with coverage of at least $1,000,000 per occurrence throughout the term of this Agreement.", "Insurance"),
    ("Each party shall maintain insurance appropriate to its obligations under this Agreement and shall provide proof of coverage upon reasonable request.", "Insurance"),
    ("Vendor shall carry professional liability (errors and omissions) insurance of not less than $500,000 and shall name Client as an additional insured.", "Insurance"),

    # ---------------- Miscellaneous / Other ----------------
    ("This Agreement constitutes the entire agreement between the parties and supersedes all prior negotiations, representations, or agreements relating to its subject matter.", "Other"),
    ("If any provision of this Agreement is held invalid or unenforceable, the remaining provisions shall continue in full force and effect.", "Other"),
    ("This Agreement may be executed in counterparts, each of which shall be deemed an original, and all of which together shall constitute one instrument.", "Other"),
    ("No waiver of any provision of this Agreement shall be effective unless in writing and signed by the party against whom the waiver is sought to be enforced.", "Other"),
]
