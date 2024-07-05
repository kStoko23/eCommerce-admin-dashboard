/* Model for extracted data of most popular subcategories,
 * contains subcategory name and count (how many was ordered from this category)
 */

export interface SubcategoriesPerYear {
  subcat_name: string;
  total_orders: number;
}
