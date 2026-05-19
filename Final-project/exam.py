     # EXAM
        elif path == "/sequence":
            eid = query.get("eid", [None])[0]
            spe = query.get("spe", [None])[0]

            if not eid or not spe:
                serve_error_page(self, 404, "Resource not available", json_response)
                return

            exam_id = eid.strip().upper()
            data_gene = get_species_from_id(exam_id)
            exam_specie = get_species_internal_name(spe)

            if not data_gene:
                serve_error_page(self, 404, "Resource not available", json_response)
                return

            species_from_id = data_gene["species"]

            if not species_from_id:
                serve_error_page(self, 404, "Resource not available", json_response)
                return

            if exam_specie != species_from_id:
                serve_error_page(self, 404, "Resource not available", json_response)
                return

            gene_name = data_gene["display_name"]
            gene_type = data_gene["object_type"]

            if not gene_name or not gene_type:
                serve_error_page(self, 404, "Resource not available", json_response)
                return

            exam_sequence = exam_get_gene_seq(exam_id, exam_specie)

            if not exam_sequence:
                serve_error_page(self, 404, "Resource not available", json_response)
                return

            exam_size = len(exam_sequence)
            exam_seq_obj = Seq(exam_sequence)
            exam_base_count = exam_seq_obj.count()

            exam_count_results = {}

            for base in "ACGT":
                count = exam_base_count[base]
                exam_count_results[base] = count

                context = {
                    "gene_id": exam_id,
                    "gene_name": gene_name,
                    "gene_type": gene_type,
                    "gene_size": exam_size,
                    "count_results": exam_count_results,
                    "exam_sequence": exam_sequence,
                }

                if json_response:
                    render_json(self, context)
                else:
                    render_html(self, "exam_result.html", context)

        # Error
        else:
            serve_error_page(self, 404, "Resource not available", json_response)
            return